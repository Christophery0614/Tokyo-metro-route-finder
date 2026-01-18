#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
东京地铁查询系统 - Flask应用
主应用文件
"""

from flask import Flask, render_template, request, jsonify, session
from dijkstra_algorithm import DijkstraAlgorithm
from tokyo_subway_data import get_station_name, get_line_name, get_station_lines
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = 'tokyo_subway_secret_key_2025'

# 初始化Dijkstra算法
dijkstra = DijkstraAlgorithm()

# 语言配置
LANGUAGES = {
    'ja': {'name': '日本語', 'flag': '🇯🇵'},
    'en': {'name': 'English', 'flag': '🇺🇸'},
    'zh': {'name': '中文', 'flag': '🇨🇳'}
}

@app.route('/')
def index():
    """主页"""
    # 设置默认语言
    if 'lang' not in session:
        session['lang'] = 'ja'
    
    lang = session['lang']
    
    return render_template('index.html', 
                          languages=LANGUAGES, 
                          current_lang=lang)

@app.route('/route')
def route_search():
    """路径查询页面"""
    lang = session.get('lang', 'ja')
    
    # 获取所有车站用于下拉菜单
    stations = dijkstra.get_all_stations(lang)
    
    return render_template('route.html', 
                          languages=LANGUAGES, 
                          current_lang=lang,
                          stations=stations)

@app.route('/lines')
def line_search():
    """线路查询页面"""
    lang = session.get('lang', 'ja')
    
    return render_template('lines.html', 
                          languages=LANGUAGES, 
                          current_lang=lang)

@app.route('/set_language/<lang>')
def set_language(lang):
    """设置语言"""
    if lang in LANGUAGES:
        session['lang'] = lang
    return jsonify({'success': True, 'language': lang})

@app.route('/search_stations')
def search_stations():
    """搜索车站"""
    keyword = request.args.get('q', '')
    lang = session.get('lang', 'ja')
    
    if not keyword:
        return jsonify([])
    
    stations = dijkstra.search_stations(keyword, lang)
    return jsonify(stations)

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    """计算最短路径"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': '无效的请求数据'}), 400
    
    start_station = data.get('start_station')
    end_station = data.get('end_station')
    lang = session.get('lang', 'ja')
    
    if not start_station or not end_station:
        return jsonify({'error': '请选择起始站和终点站'}), 400
    
    # 计算最短路径
    path, total_time = dijkstra.find_shortest_path(start_station, end_station)
    
    if not path:
        return jsonify({'error': '未找到从起始站到终点站的路径'}), 404
    
    # 获取路径详情
    path_details = dijkstra.get_path_details(path, lang)
    
    # 计算时间信息
    from datetime import datetime, timedelta
    import pytz
    
    # 获取当前东京时间
    tokyo_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(tokyo_tz)
    
    # 计算出发时间和到达时间
    departure_time = current_time
    arrival_time = current_time + timedelta(minutes=total_time)
    
    # 格式化时间显示
    time_format = {
        'ja': '%Y年%m月%d日 %H時%M分',
        'en': '%Y-%m-%d %H:%M',
        'zh': '%Y年%m月%d日 %H时%M分'
    }.get(lang, '%Y-%m-%d %H:%M')
    
    # 准备响应数据
    result = {
        'success': True,
        'total_time': total_time,
        'path_details': path_details,
        'start_station': get_station_name(start_station, lang),
        'end_station': get_station_name(end_station, lang),
        'time_info': {
            'departure_time': departure_time.strftime(time_format),
            'arrival_time': arrival_time.strftime(time_format),
            'current_time': current_time.strftime(time_format),
            'travel_time': total_time
        }
    }
    
    return jsonify(result)

@app.route('/station_info/<station_id>')
def station_info(station_id):
    """获取车站详细信息"""
    lang = session.get('lang', 'ja')
    
    station_name = get_station_name(station_id, lang)
    lines = get_station_lines(station_id)
    line_names = [get_line_name(line, lang) for line in lines]
    
    info = {
        'id': station_id,
        'name': station_name,
        'lines': line_names,
        'line_codes': lines
    }
    
    return jsonify(info)

@app.route('/current_time')
def current_time():
    """获取当前服务器时间"""
    from datetime import datetime
    import pytz
    
    # 获取东京时间
    tokyo_tz = pytz.timezone('Asia/Tokyo')
    tokyo_time = datetime.now(tokyo_tz)
    
    # 格式化的时间字符串
    time_info = {
        'server_time': tokyo_time.isoformat(),
        'tokyo_time': tokyo_time.strftime('%Y-%m-%d %H:%M:%S'),
        'unix_timestamp': int(tokyo_time.timestamp()),
        'timezone': 'Asia/Tokyo',
        'timezone_offset': tokyo_time.strftime('%z')
    }
    
    return jsonify(time_info)

@app.route('/line_stations/<line_code>')
def line_stations(line_code):
    """获取特定线路的车站列表"""
    lang = session.get('lang', 'ja')
    
    # 获取线路的车站运行顺序
    from tokyo_subway_data import get_line_station_order
    station_order = get_line_station_order(line_code)
    
    stations = []
    
    # 按运行顺序排列车站
    for station_id in station_order:
        station_lines = get_station_lines(station_id)
        if line_code in station_lines:
            station_name = get_station_name(station_id, lang)
            stations.append({
                'id': station_id,
                'name': station_name,
                'lines': station_lines,
                'order': len(stations) + 1  # 添加顺序编号
            })
    
    # 如果没有找到顺序，按名称排序作为备用
    if not stations:
        from tokyo_subway_data import TOKYO_SUBWAY_STATIONS
        for station_id in TOKYO_SUBWAY_STATIONS['ja'].keys():
            station_lines = get_station_lines(station_id)
            if line_code in station_lines:
                station_name = get_station_name(station_id, lang)
                stations.append({
                    'id': station_id,
                    'name': station_name,
                    'lines': station_lines,
                    'order': len(stations) + 1
                })
        stations.sort(key=lambda x: x['name'])
    
    return jsonify(stations)

@app.route('/about')
def about():
    """关于页面"""
    lang = session.get('lang', 'ja')
    
    about_texts = {
        'ja': {
            'title': '東京地下鉄検索システムについて',
            'description': 'このシステムはDijkstraアルゴリズムを使用して、東京地下鉄の最短経路を計算します。',
            'features': [
                '最短経路検索',
                '駅情報表示',
                '多言語対応（日本語、英語、中国語）',
                'リアルタイム検索'
            ]
        },
        'en': {
            'title': 'About Tokyo Subway Search System',
            'description': 'This system uses Dijkstra algorithm to calculate the shortest path in Tokyo subway.',
            'features': [
                'Shortest path search',
                'Station information display',
                'Multi-language support (Japanese, English, Chinese)',
                'Real-time search'
            ]
        },
        'zh': {
            'title': '关于东京地铁查询系统',
            'description': '本系统使用Dijkstra算法计算东京地铁的最短路径。',
            'features': [
                '最短路径查询',
                '车站信息显示',
                '多语言支持（日语、英语、中文）',
                '实时搜索'
            ]
        }
    }
    
    about_info = about_texts.get(lang, about_texts['ja'])
    
    return render_template('about.html', 
                          languages=LANGUAGES, 
                          current_lang=lang,
                          about_info=about_info)

# 错误处理
@app.errorhandler(404)
def not_found(error):
    lang = session.get('lang', 'ja')
    
    error_messages = {
        'ja': 'ページが見つかりません',
        'en': 'Page not found',
        'zh': '页面未找到'
    }
    
    return render_template('error.html', 
                          error_message=error_messages.get(lang, 'Page not found'),
                          languages=LANGUAGES,
                          current_lang=lang), 404

@app.errorhandler(500)
def internal_error(error):
    lang = session.get('lang', 'ja')
    
    error_messages = {
        'ja': '内部サーバーエラー',
        'en': 'Internal server error',
        'zh': '内部服务器错误'
    }
    
    return render_template('error.html', 
                          error_message=error_messages.get(lang, 'Internal server error'),
                          languages=LANGUAGES,
                          current_lang=lang), 500

@app.route('/export_panorama')
def export_panorama():
    """导出全景图为PDF"""
    try:
        from io import BytesIO
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from datetime import datetime
        
        # 创建PDF缓冲区
        buffer = BytesIO()
        
        # 创建PDF文档
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        
        # 设置标题
        lang = session.get('lang', 'ja')
        
        # 多语言标题
        titles = {
            'ja': '東京地下鉄路線全景図',
            'en': 'Tokyo Subway Panorama Map',
            'zh': '东京地铁线路全景图'
        }
        
        title = titles.get(lang, titles['ja'])
        
        # 绘制标题
        p.setFont("Helvetica-Bold", 24)
        p.drawCentredString(width/2, height - 50, title)
        
        # 绘制副标题
        p.setFont("Helvetica", 14)
        p.drawCentredString(width/2, height - 80, "Tokyo Subway System")
        
        # 绘制日期
        now = datetime.now()
        date_str = now.strftime('%Y年%m月%d日 %H:%M')
        p.setFont("Helvetica", 10)
        p.drawString(50, height - 100, f"生成日時: {date_str}")
        
        # 绘制说明文字
        explanations = {
            'ja': '※ この図は東京地下鉄13路線の概要を示しています',
            'en': '※ This diagram shows an overview of 13 Tokyo subway lines',
            'zh': '※ 此图展示了东京地铁13条线路的概况'
        }
        explanation = explanations.get(lang, explanations['ja'])
        p.drawString(50, height - 120, explanation)
        
        # 绘制线路图例（简化版）
        line_data = {
            'G': {'name': '銀座線', 'color': '#FF9500'},
            'M': {'name': '丸ノ内線', 'color': '#E60012'},
            'H': {'name': '日比谷線', 'color': '#B5B5AC'},
            'T': {'name': '東西線', 'color': '#009BBF'},
            'C': {'name': '千代田線', 'color': '#00BB85'},
            'Y': {'name': '有楽町線', 'color': '#C1A470'},
            'Z': {'name': '半蔵門線', 'color': '#8F76D6'},
            'N': {'name': '南北線', 'color': '#00AC9B'},
            'F': {'name': '副都心線', 'color': '#9C5E31'},
            'A': {'name': '浅草線', 'color': '#E85298'},
            'I': {'name': '三田線', 'color': '#0079C2'},
            'S': {'name': '新宿線', 'color': '#6CBB5A'},
            'E': {'name': '大江戸線', 'color': '#B6007A'}
        }
        
        # 绘制图例
        legend_y = height - 180
        p.setFont("Helvetica-Bold", 12)
        p.drawString(50, legend_y, "路線一覧:")
        
        legend_y -= 20
        p.setFont("Helvetica", 10)
        
        # 分两列显示线路
        col1_x, col2_x = 50, width/2 + 50
        current_y = legend_y
        
        for i, (line_code, info) in enumerate(line_data.items()):
            if i < 6:
                x_pos = col1_x
                y_pos = current_y - i * 15
            else:
                x_pos = col2_x
                y_pos = legend_y - (i - 6) * 15
            
            # 绘制线路颜色方块
            p.setFillColor(info['color'])
            p.rect(x_pos, y_pos, 15, 8, fill=1, stroke=0)
            
            # 绘制线路名称
            p.setFillColor(colors.black)
            p.drawString(x_pos + 20, y_pos - 2, f"{line_code}線 - {info['name']}")
        
        # 绘制简单的线路示意图
        diagram_y = height - 300
        p.setFont("Helvetica-Bold", 14)
        p.drawCentredString(width/2, diagram_y, "路線配置図")
        
        # 绘制简化线路图
        diagram_y -= 30
        
        # 绘制线路示意线（基于真实布局）
        p.setLineWidth(3)
        
        # 银座线（东西向）
        p.setStrokeColor(line_data['G']['color'])
        p.line(150, diagram_y - 100, 950, diagram_y - 130)
        
        # 丸之内线（环形）
        p.setStrokeColor(line_data['M']['color'])
        p.line(400, diagram_y - 50, 450, diagram_y - 20)
        p.line(450, diagram_y - 20, 500, diagram_y - 10)
        p.line(500, diagram_y - 10, 550, diagram_y - 20)
        p.line(550, diagram_y - 20, 600, diagram_y - 50)
        
        # 日比谷线（南北向）
        p.setStrokeColor(line_data['H']['color'])
        p.line(550, diagram_y - 40, 450, diagram_y - 160)
        
        # 大江户线（环形）
        p.setStrokeColor(line_data['E']['color'])
        center_x, center_y = width/2, diagram_y - 100
        radius = 40
        p.circle(center_x, center_y, radius)
        
        # 添加说明
        diagram_y -= 170
        p.setFont("Helvetica", 10)
        p.setFillColor(colors.black)
        
        notes = {
            'ja': '※ 実際の路線配置は複雑なネットワークを形成しています',
            'en': '※ Actual line configuration forms a complex network',
            'zh': '※ 实际线路配置形成了复杂的网络结构'
        }
        note = notes.get(lang, notes['ja'])
        p.drawCentredString(width/2, diagram_y, note)
        
        # 完成PDF
        p.showPage()
        p.save()
        
        # 获取PDF数据
        buffer.seek(0)
        pdf_data = buffer.getvalue()
        buffer.close()
        
        # 创建响应
        from flask import make_response
        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=tokyo_subway_panorama_{now.strftime("%Y%m%d_%H%M")}.pdf'
        
        return response
        
    except Exception as e:
        print(f"PDF生成错误: {e}")
        return jsonify({'error': 'PDF生成失败，请检查reportlab库是否安装'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)