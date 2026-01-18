#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dijkstra算法实现模块
用于计算东京地铁最短路径
"""

import heapq
from typing import Dict, List, Tuple, Optional
from tokyo_subway_data import build_subway_graph, get_station_name, get_line_name, get_station_lines

class DijkstraAlgorithm:
    """Dijkstra算法实现类"""
    
    def __init__(self):
        self.graph = build_subway_graph()
    
    def find_shortest_path(self, start_station: str, end_station: str) -> Tuple[Optional[List[str]], Optional[int]]:
        """
        使用Dijkstra算法查找最短路径
        
        Args:
            start_station: 起始车站ID
            end_station: 终点车站ID
            
        Returns:
            Tuple[路径列表, 总时间] 或 (None, None) 如果路径不存在
        """
        # 验证车站是否存在
        if start_station not in self.graph or end_station not in self.graph:
            return None, None
        
        # 初始化距离字典
        distances = {station: float('inf') for station in self.graph}
        distances[start_station] = 0
        
        # 初始化前驱节点字典
        previous = {station: None for station in self.graph}
        
        # 优先队列（最小堆）
        priority_queue = [(0, start_station)]
        
        while priority_queue:
            current_distance, current_station = heapq.heappop(priority_queue)
            
            # 如果找到终点站，提前结束
            if current_station == end_station:
                break
            
            # 如果当前距离大于已知最短距离，跳过
            if current_distance > distances[current_station]:
                continue
            
            # 遍历相邻车站
            for neighbor, time in self.graph[current_station].items():
                distance = current_distance + time
                
                # 如果找到更短路径
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_station
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # 如果终点站不可达
        if distances[end_station] == float('inf'):
            return None, None
        
        # 重构路径
        path = []
        current = end_station
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        
        return path, distances[end_station]
    
    def get_path_details(self, path: List[str], lang: str = 'ja') -> List[Dict]:
        """
        获取路径详细信息
        
        Args:
            path: 路径列表
            lang: 语言代码 ('ja', 'en', 'zh')
            
        Returns:
            包含详细信息的字典列表
        """
        if not path:
            return []
        
        details = []
        
        for i in range(len(path)):
            station_id = path[i]
            station_name = get_station_name(station_id, lang)
            lines = get_station_lines(station_id)
            line_names = [get_line_name(line, lang) for line in lines]
            
            detail = {
                'station_id': station_id,
                'station_name': station_name,
                'line_codes': lines,
                'line_names': line_names,
                'order': i + 1
            }
            
            # 如果是换乘站，添加换乘信息
            if i > 0:
                prev_station_id = path[i-1]
                prev_lines = get_station_lines(prev_station_id)
                
                # 检查是否换乘
                if not set(lines).intersection(set(prev_lines)):
                    detail['transfer'] = True
                    detail['transfer_from'] = [get_line_name(line, lang) for line in prev_lines]
                    detail['transfer_to'] = line_names
                else:
                    detail['transfer'] = False
            else:
                detail['transfer'] = False
            
            details.append(detail)
        
        return details
    
    def get_all_stations(self, lang: str = 'ja') -> List[Dict]:
        """
        获取所有车站信息
        
        Args:
            lang: 语言代码
            
        Returns:
            车站信息列表
        """
        stations = []
        
        for station_id in self.graph.keys():
            station_name = get_station_name(station_id, lang)
            lines = get_station_lines(station_id)
            line_names = [get_line_name(line, lang) for line in lines]
            
            stations.append({
                'id': station_id,
                'name': station_name,
                'lines': line_names,
                'line_codes': lines
            })
        
        # 按名称排序
        stations.sort(key=lambda x: x['name'])
        return stations
    
    def search_stations(self, keyword: str, lang: str = 'ja') -> List[Dict]:
        """
        搜索车站
        
        Args:
            keyword: 搜索关键词
            lang: 语言代码
            
        Returns:
            匹配的车站列表，按匹配优先级排序
        """
        all_stations = self.get_all_stations(lang)
        matches = []
        
        # 获取所有语言的车站名称用于跨语言搜索
        from tokyo_subway_data import TOKYO_SUBWAY_STATIONS
        
        for station in all_stations:
            station_id = station['id']
            
            # 检查当前语言的车站名称
            current_name = station['name'].lower()
            
            # 检查其他语言的车站名称
            ja_name = TOKYO_SUBWAY_STATIONS['ja'].get(station_id, '').lower()
            en_name = TOKYO_SUBWAY_STATIONS['en'].get(station_id, '').lower()
            zh_name = TOKYO_SUBWAY_STATIONS['zh'].get(station_id, '').lower()
            
            keyword_lower = keyword.lower()
            match_score = 0
            
            # 多语言搜索：在当前语言、日语、英语、中文中搜索
            # 完全匹配得最高分
            if current_name == keyword_lower or ja_name == keyword_lower:
                match_score = 100
            elif en_name == keyword_lower or zh_name == keyword_lower:
                match_score = 90
            # 开头匹配得高分
            elif current_name.startswith(keyword_lower) or ja_name.startswith(keyword_lower):
                match_score = 80
            elif en_name.startswith(keyword_lower) or zh_name.startswith(keyword_lower):
                match_score = 70
            # 包含匹配得中等分
            elif keyword_lower in current_name or keyword_lower in ja_name:
                match_score = 60
            elif keyword_lower in en_name or keyword_lower in zh_name:
                match_score = 50
            # 在线路名称中搜索得低分
            elif any(keyword_lower in line.lower() for line in station['lines']):
                match_score = 30
            else:
                continue
                
            # 为新宿站特别处理（日语汉字和片假名都可能）
            if station_id == 'Shinjuku' and ('新宿' in keyword or 'しんじゅく' in keyword_lower):
                match_score = 100
            
            matches.append((match_score, station))
        
        # 按匹配分数降序排序，分数相同的按字母顺序排序
        matches.sort(key=lambda x: (-x[0], x[1]['name']))
        
        # 只返回车站信息，不包含分数
        return [station for score, station in matches]

def test_dijkstra():
    """测试Dijkstra算法"""
    dijkstra = DijkstraAlgorithm()
    
    # 测试路径查找
    start = 'Shibuya_G'
    end = 'Ueno_H'
    
    path, total_time = dijkstra.find_shortest_path(start, end)
    
    if path:
        print(f"从 {get_station_name(start)} 到 {get_station_name(end)} 的最短路径:")
        print(f"总时间: {total_time} 分钟")
        print("路径详情:")
        
        details = dijkstra.get_path_details(path)
        for detail in details:
            station_info = f"{detail['order']}. {detail['station_name']}"
            if detail['transfer']:
                station_info += f" (换乘: {' → '.join(detail['transfer_to'])})"
            print(station_info)
    else:
        print("未找到路径")

if __name__ == "__main__":
    test_dijkstra()