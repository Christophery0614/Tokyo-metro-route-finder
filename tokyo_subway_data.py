#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
东京地铁数据模块
包含东京地铁线路、车站和连接关系的真实数据
支持中英日三语
"""

# 东京地铁线路数据（真实数据 - 13条线路）
TOKYO_SUBWAY_LINES = {
    'ja': {
        # 东京地铁（9条）
        'G': '銀座線',
        'M': '丸ノ内線',
        'H': '日比谷線',
        'T': '東西線',
        'C': '千代田線',
        'Y': '有楽町線',
        'Z': '半蔵門線',
        'N': '南北線',
        'F': '副都心線',
        # 都营地铁（4条）
        'A': '浅草線',
        'I': '三田線',
        'S': '新宿線',
        'E': '大江戸線'
    },
    'en': {
        # 东京地铁（9条）
        'G': 'Ginza Line',
        'M': 'Marunouchi Line',
        'H': 'Hibiya Line',
        'T': 'Tozai Line',
        'C': 'Chiyoda Line',
        'Y': 'Yurakucho Line',
        'Z': 'Hanzomon Line',
        'N': 'Namboku Line',
        'F': 'Fukutoshin Line',
        # 都营地铁（4条）
        'A': 'Asakusa Line',
        'I': 'Mita Line',
        'S': 'Shinjuku Line',
        'E': 'Oedo Line'
    },
    'zh': {
        # 东京地铁（9条）
        'G': '银座线',
        'M': '丸之内线',
        'H': '日比谷线',
        'T': '东西线',
        'C': '千代田线',
        'Y': '有乐町线',
        'Z': '半藏门线',
        'N': '南北线',
        'F': '副都心线',
        # 都营地铁（4条）
        'A': '浅草线',
        'I': '三田线',
        'S': '新宿线',
        'E': '大江户线'
    }
}

# 东京地铁车站数据（完整数据）
TOKYO_SUBWAY_STATIONS = {
    'ja': {
        # 银座线 (19駅)
        'Shibuya_G': '渋谷', 'Omotesando_G': '表参道', 'AoyamaItchome_G': '青山一丁目', 'Gaiemmae_G': '外苑前', 
        'AkasakaMitsuke_G': '赤坂見附', 'TameikeSanno_G': '溜池山王', 'Toranomon_G': '虎ノ門', 'Shimbashi_G': '新橋',
        'Ginza_G': '銀座', 'Kyobashi_G': '京橋', 'Nihonbashi_G': '日本橋', 'Mitsukoshimae_G': '三越前',
        'Kanda_G': '神田', 'Suehirocho_G': '末広町', 'Uenohirokoji_G': '上野広小路', 'Ueno_G': '上野',
        'Inaricho_G': '稲荷町', 'Tawaramachi_G': '田原町', 'Asakusa_G': '浅草',
        
        # 丸之内线 (28駅)
        'Ogikubo_M': '荻窪', 'MinamiAsagaya_M': '南阿佐ヶ谷', 'Shinkoenji_M': '新高円寺', 'Higashikoenji_M': '東高円寺',
        'ShinNakano_M': '新中野', 'NakanoFujimicho_M': '中野富士見町', 'NakanoShimbashi_M': '中野新橋', 'NakanoSakaue_M': '中野坂上',
        'NishiShinjuku_M': '西新宿', 'Shinjuku_M': '新宿', 'ShinjukuSanchome_M': '新宿三丁目', 'ShinjukuGyoemmae_M': '新宿御苑前',
        'YotsuyaSanchome_M': '四谷三丁目', 'Yotsuya_M': '四谷', 'AkasakaMitsuke_M': '赤坂見附', 'KokkaiGijidomae_M': '国会議事堂前',
        'Kasumigaseki_M': '霞ヶ関', 'Ginza_M': '銀座', 'Tokyo_M': '東京', 'Otemachi_M': '大手町',
        'Awajicho_M': '淡路町', 'Ochanomizu_M': '御茶ノ水', 'Hongosanchome_M': '本郷三丁目', 'Korakuen_M': '後楽園',
        'Myogadani_M': '茗荷谷', 'Shinotsuka_M': '新大塚', 'Ikebukuro_M': '池袋',
        
        # 日比谷线 (21駅)
        'NakaMeguro_H': '中目黒', 'Ebisu_H': '恵比寿', 'Hiroo_H': '広尾', 'Roppongi_H': '六本木',
        'Kamiyacho_H': '神谷町', 'Kasumigaseki_H': '霞ヶ関', 'Hibiya_H': '日比谷', 'Ginza_H': '銀座',
        'HigashiGinza_H': '東銀座', 'Tsukiji_H': '築地', 'Hatchobori_H': '八丁堀', 'Kayabacho_H': '茅場町',
        'Nihonbashi_H': '日本橋', 'Mitsukoshimae_H': '三越前', 'Kanda_H': '神田', 'Akihabara_H': '秋葉原',
        'NakaOkachimachi_H': '仲御徒町', 'Ueno_H': '上野', 'Iriya_H': '入谷', 'Minowa_H': '三ノ輪',
        'MinamiSenju_H': '南千住', 'KitaSenju_H': '北千住',
        
        # 东西线 (23駅)
        'Nakano_T': '中野', 'Ochiai_T': '落合', 'Takadanobaba_T': '高田馬場', 'Waseda_T': '早稲田',
        'Kagurazaka_T': '神楽坂', 'Iidabashi_T': '飯田橋', 'Kudanshita_T': '九段下', 'Takebashi_T': '竹橋',
        'Otemachi_T': '大手町', 'Nihonbashi_T': '日本橋', 'Kayabacho_T': '茅場町', 'MonzenNakacho_T': '門前仲町',
        'Kiba_T': '木場', 'Toyocho_T': '豊洲', 'MinamiSunamachi_T': '南砂町', 'Shinkiba_T': '新木場',
        'NishiFunabashi_T': '西船橋', 'Funabashi_T': '船橋', 'Tsudanuma_T': '津田沼', 'Myoden_T': '妙典',
        'Barakinakayama_T': '原木中山', 'Hirai_T': '平井', 'Koiwa_T': '小岩',
        
        # 千代田线 (20駅)
        'YoyogiUehara_C': '代々木上原', 'YoyogiKohen_C': '代々木公園', 'MeijiJingumae_C': '明治神宮前', 'Omotesando_C': '表参道',
        'Nogizaka_C': '乃木坂', 'Akasaka_C': '赤坂', 'KokkaiGijidomae_C': '国会議事堂前', 'Kasumigaseki_C': '霞ヶ関',
        'Hibiya_C': '日比谷', 'Nijubashimae_C': '二重橋前', 'Otemachi_C': '大手町', 'ShinOchanomizu_C': '新御茶ノ水',
        'Yushima_C': '湯島', 'Nezu_C': '根津', 'Sendagi_C': '千駄木', 'NishiNippori_C': '西日暮里',
        'Machiya_C': '町屋', 'KitaSenju_C': '北千住', 'Ayase_C': '綾瀬',
        
        # 有乐町线 (24駅)
        'Wakoshi_Y': '和光市', 'ChikatetsuAkatsuka_Y': '地下鉄赤塚', 'Heiwadai_Y': '平和台', 'Hikawadai_Y': '氷川台',
        'KotakeMukaihara_Y': '小竹向原', 'Senkawa_Y': '千川', 'Kanamecho_Y': '要町', 'Ikebukuro_Y': '池袋',
        'HigashiIkebukuro_Y': '東池袋', 'Gokokuji_Y': '護国寺', 'Edogawabashi_Y': '江戸川橋', 'Iidabashi_Y': '飯田橋',
        'Ichigaya_Y': '市ヶ谷', 'Kojimachi_Y': '麹町', 'Nagatacho_Y': '永田町', 'Sakuradamon_Y': '桜田門',
        'Yurakucho_Y': '有楽町', 'GinzaItchome_Y': '銀座一丁目', 'Shintomicho_Y': '新富町', 'Tsukishima_Y': '月島',
        'Toyosu_Y': '豊洲', 'Tatsumi_Y': '辰巳', 'ShinKiba_Y': '新木場',
        
        # 半藏门线 (14駅)
        'Shibuya_Z': '渋谷', 'Omotesando_Z': '表参道', 'AoyamaItchome_Z': '青山一丁目', 'Nagatacho_Z': '永田町',
        'Hanzomon_Z': '半蔵門', 'Kudanshita_Z': '九段下', 'Jimbocho_Z': '神保町', 'Otemachi_Z': '大手町',
        'Mitsukoshimae_Z': '三越前', 'Suitengumae_Z': '水天宮前', 'KiyosumiShirakawa_Z': '清澄白河', 'Sumiyoshi_Z': '住吉',
        'Kinshicho_Z': '錦糸町', 'Oshiage_Z': '押上',
        
        # 南北线 (19駅)
        'Meguro_N': '目黒', 'Shirokanedai_N': '白金台', 'ShirokaneTakanawa_N': '白金高輪', 'AzabuJuban_N': '麻布十番',
        'RoppongiItchome_N': '六本木一丁目', 'TameikeSanno_N': '溜池山王', 'Nagatacho_N': '永田町', 'Yotsuya_N': '四谷',
        'Ichigaya_N': '市ヶ谷', 'Idabashi_N': '飯田橋', 'Korakuen_N': '後楽園', 'Todaimae_N': '東大前',
        'HonKomagome_N': '本駒込', 'Komagome_N': '駒込', 'Nishigahara_N': '西ヶ原', 'Oji_N': '王子',
        'OjiKamiya_N': '王子神谷', 'Shimo_N': '志茂', 'AkabaneIwabuchi_N': '赤羽岩淵',
        
        # 副都心线 (16駅)
        'Wakoshi_F': '和光市', 'ChikatetsuAkatsuka_F': '地下鉄赤塚', 'Heiwadai_F': '平和台', 'Hikawadai_F': '氷川台',
        'KotakeMukaihara_F': '小竹向原', 'Senkawa_F': '千川', 'Kanamecho_F': '要町', 'Ikebukuro_F': '池袋',
        'Zoshigaya_F': '雑司が谷', 'NishiWaseda_F': '西早稲田', 'HigashiShinjuku_F': '東新宿', 'ShinjukuSanchome_F': '新宿三丁目',
        'Kitasando_F': '北参道', 'MeijiJingumae_F': '明治神宮前', 'Shibuya_F': '渋谷',
        
        # 浅草线 (20駅)
        'NishiMagome_A': '西馬込', 'Magome_A': '馬込', 'Nakanobu_A': '中延', 'Togoshi_A': '戸越', 'Gotanda_A': '五反田',
        'Takanawadai_A': '高輪台', 'Sengakuji_A': '泉岳寺', 'Mita_A': '三田', 'Daimon_A': '大門', 'Shimbashi_A': '新橋',
        'HigashiGinza_A': '東銀座', 'Nihonbashi_A': '日本橋', 'Ningyocho_A': '人形町', 'HigashiNihonbashi_A': '東日本橋',
        'Asakusabashi_A': '浅草橋', 'Kuramae_A': '蔵前', 'Asakusa_A': '浅草', 'HonjoAzumabashi_A': '本所吾妻橋',
        'Oshiage_A': '押上',
        
        # 三田线 (27駅)
        'NishiTakashimadaira_I': '西高島平', 'Takashimadaira_I': '高島平', 'ShimuraSakaue_I': '志村坂上', 'ShimuraSanchome_I': '志村三丁目',
        'Hasune_I': '蓮根', 'Nishidai_I': '西台', 'TakashimadairaKoen_I': '高島平公園', 'ShinItabashi_I': '新板橋', 'ItabashiKuyakushomae_I': '板橋区役所前',
        'ItabashiHoncho_I': '板橋本町', 'Motohasunuma_I': '本蓮沼', 'Shimura_I': '志村', 'Nishigahara_I': '西ヶ原', 'Oji_I': '王子',
        'OjiKamiya_I': '王子神谷', 'Shimo_I': '志茂', 'AkabaneIwabuchi_I': '赤羽岩淵', 'Sugamo_I': '巣鴨', 'NishiSugamo_I': '西巣鴨',
        'ShinKoshinzuka_I': '新庚申塚', 'HigashiIkebukuro_I': '東池袋', 'Kasuga_I': '春日', 'Hakusan_I': '白山', 'Sengoku_I': '千石',
        'Sugamo_I': '巣鴨', 'NishiSugamo_I': '西巣鴨', 'ShinKoshinzuka_I': '新庚申塚',
        
        # 新宿线 (21駅)
        'Motoyawata_S': '本八幡', 'IchikawaShibayama_S': '市川塩浜', 'Funabori_S': '船堀', 'ShinKoiwa_S': '新小岩', 'HigashiOjima_S': '東大島',
        'Ojima_S': '大島', 'Sumiyoshi_S': '住吉', 'NishiOjima_S': '西大島', 'Kikukawa_S': '菊川', 'ShinOjima_S': '新大島', 'Morishita_S': '森下',
        'Hamacho_S': '浜町', 'Bakuroyokoyama_S': '馬喰横山', 'Iwamotocho_S': '岩本町', 'Ogawamachi_S': '小川町', 'ShinOchanomizu_S': '新御茶ノ水',
        'Jimbocho_S': '神保町', 'Kudanshita_S': '九段下', 'Ichigaya_S': '市ヶ谷', 'YotsuyaSanchome_S': '四谷三丁目', 'Shinjuku_S': '新宿',
        
        # 大江户线 (38駅)
        'TochoMae_E': '都庁前', 'ShinjukuNishiguchi_E': '新宿西口', 'HigashiShinjuku_E': '東新宿', 'WakamatsuKawada_E': '若松河田',
        'UshigomeYanagicho_E': '牛込柳町', 'UshigomeKagurazaka_E': '牛込神楽坂', 'Iidabashi_E': '飯田橋', 'Kasuga_E': '春日',
        'Hongosanchome_E': '本郷三丁目', 'UenoOkachimachi_E': '上野御徒町', 'ShinOkachimachi_E': '新御徒町', 'Kuramae_E': '蔵前',
        'Ryogoku_E': '両国', 'Morishita_E': '森下', 'KiyosumiShirakawa_E': '清澄白河', 'MonzenNakacho_E': '門前仲町',
        'Tsukishima_E': '月島', 'Kachidoki_E': '勝どき', 'Tsukijishijo_E': '築地市場', 'Shiodome_E': '汐留', 'Daimon_E': '大門',
        'Akabanebashi_E': '赤羽橋', 'AzabuJuban_E': '麻布十番', 'Roppongi_E': '六本木', 'AoyamaItchome_E': '青山一丁目',
        'KokuritsuKyougijo_E': '国立競技場', 'Yoyogi_E': '代々木', 'Shinjuku_E': '新宿', 'TochoMae_E': '都庁前'
    },
    'en': {
        # Ginza Line (19 stations)
        'Shibuya_G': 'Shibuya', 'Omotesando_G': 'Omotesando', 'AoyamaItchome_G': 'Aoyama-itchome', 'Gaiemmae_G': 'Gaiemmae', 
        'AkasakaMitsuke_G': 'Akasaka-mitsuke', 'TameikeSanno_G': 'Tameike-sanno', 'Toranomon_G': 'Toranomon', 'Shimbashi_G': 'Shimbashi',
        'Ginza_G': 'Ginza', 'Kyobashi_G': 'Kyobashi', 'Nihonbashi_G': 'Nihonbashi', 'Mitsukoshimae_G': 'Mitsukoshimae',
        'Kanda_G': 'Kanda', 'Suehirocho_G': 'Suehirocho', 'Uenohirokoji_G': 'Ueno-hirokoji', 'Ueno_G': 'Ueno',
        'Inaricho_G': 'Inaricho', 'Tawaramachi_G': 'Tawaramachi', 'Asakusa_G': 'Asakusa',
        
        # Marunouchi Line (28 stations)
        'Ogikubo_M': 'Ogikubo', 'MinamiAsagaya_M': 'Minami-asagaya', 'Shinkoenji_M': 'Shin-koenji', 'Higashikoenji_M': 'Higashi-koenji',
        'ShinNakano_M': 'Shin-nakano', 'NakanoFujimicho_M': 'Nakano-fujimicho', 'NakanoShimbashi_M': 'Nakano-shimbashi', 'NakanoSakaue_M': 'Nakano-sakaue',
        'NishiShinjuku_M': 'Nishi-shinjuku', 'Shinjuku_M': 'Shinjuku', 'ShinjukuSanchome_M': 'Shinjuku-sanchome', 'ShinjukuGyoemmae_M': 'Shinjuku-gyoemmae',
        'YotsuyaSanchome_M': 'Yotsuya-sanchome', 'Yotsuya_M': 'Yotsuya', 'AkasakaMitsuke_M': 'Akasaka-mitsuke', 'KokkaiGijidomae_M': 'Kokkai-gijidomae',
        'Kasumigaseki_M': 'Kasumigaseki', 'Ginza_M': 'Ginza', 'Tokyo_M': 'Tokyo', 'Otemachi_M': 'Otemachi',
        'Awajicho_M': 'Awajicho', 'Ochanomizu_M': 'Ochanomizu', 'Hongosanchome_M': 'Hongo-sanchome', 'Korakuen_M': 'Korakuen',
        'Myogadani_M': 'Myogadani', 'Shinotsuka_M': 'Shin-otsuka', 'Ikebukuro_M': 'Ikebukuro',
        
        # Hibiya Line (21 stations)
        'NakaMeguro_H': 'Nakameguro', 'Ebisu_H': 'Ebisu', 'Hiroo_H': 'Hiroo', 'Roppongi_H': 'Roppongi',
        'Kamiyacho_H': 'Kamiyacho', 'Kasumigaseki_H': 'Kasumigaseki', 'Hibiya_H': 'Hibiya', 'Ginza_H': 'Ginza',
        'HigashiGinza_H': 'Higashi-ginza', 'Tsukiji_H': 'Tsukiji', 'Hatchobori_H': 'Hatchobori', 'Kayabacho_H': 'Kayabacho',
        'Nihonbashi_H': 'Nihonbashi', 'Mitsukoshimae_H': 'Mitsukoshimae', 'Kanda_H': 'Kanda', 'Akihabara_H': 'Akihabara',
        'NakaOkachimachi_H': 'Naka-okachimachi', 'Ueno_H': 'Ueno', 'Iriya_H': 'Iriya', 'Minowa_H': 'Minowa',
        'MinamiSenju_H': 'Minami-senju', 'KitaSenju_H': 'Kita-senju',
        
        # Tozai Line (23 stations)
        'Nakano_T': 'Nakano', 'Ochiai_T': 'Ochiai', 'Takadanobaba_T': 'Takadanobaba', 'Waseda_T': 'Waseda',
        'Kagurazaka_T': 'Kagurazaka', 'Iidabashi_T': 'Iidabashi', 'Kudanshita_T': 'Kudanshita', 'Takebashi_T': 'Takebashi',
        'Otemachi_T': 'Otemachi', 'Nihonbashi_T': 'Nihonbashi', 'Kayabacho_T': 'Kayabacho', 'MonzenNakacho_T': 'Monzen-nakacho',
        'Kiba_T': 'Kiba', 'Toyocho_T': 'Toyocho', 'MinamiSunamachi_T': 'Minami-sunamachi', 'Shinkiba_T': 'Shinkiba',
        'NishiFunabashi_T': 'Nishi-funabashi', 'Funabashi_T': 'Funabashi', 'Tsudanuma_T': 'Tsudanuma', 'Myoden_T': 'Myoden',
        'Barakinakayama_T': 'Baraki-nakayama', 'Hirai_T': 'Hirai', 'Koiwa_T': 'Koiwa',
        
        # Chiyoda Line (20 stations)
        'YoyogiUehara_C': 'Yoyogi-uehara', 'YoyogiKohen_C': 'Yoyogi-koen', 'MeijiJingumae_C': 'Meiji-jingumae', 'Omotesando_C': 'Omotesando',
        'Nogizaka_C': 'Nogizaka', 'Akasaka_C': 'Akasaka', 'KokkaiGijidomae_C': 'Kokkai-gijidomae', 'Kasumigaseki_C': 'Kasumigaseki',
        'Hibiya_C': 'Hibiya', 'Nijubashimae_C': 'Nijubashimae', 'Otemachi_C': 'Otemachi', 'ShinOchanomizu_C': 'Shin-ochinomizu',
        'Yushima_C': 'Yushima', 'Nezu_C': 'Nezu', 'Sendagi_C': 'Sendagi', 'NishiNippori_C': 'Nishi-nippori',
        'Machiya_C': 'Machiya', 'KitaSenju_C': 'Kita-senju', 'Ayase_C': 'Ayase',
        
        # Yurakucho Line (24 stations)
        'Wakoshi_Y': 'Wakoshi', 'ChikatetsuAkatsuka_Y': 'Chikatetsu-akatsuka', 'Heiwadai_Y': 'Heiwadai', 'Hikawadai_Y': 'Hikawadai',
        'KotakeMukaihara_Y': 'Kotake-mukaihara', 'Senkawa_Y': 'Senkawa', 'Kanamecho_Y': 'Kanamecho', 'Ikebukuro_Y': 'Ikebukuro',
        'HigashiIkebukuro_Y': 'Higashi-ikebukuro', 'Gokokuji_Y': 'Gokokuji', 'Edogawabashi_Y': 'Edogawabashi', 'Iidabashi_Y': 'Iidabashi',
        'Ichigaya_Y': 'Ichigaya', 'Kojimachi_Y': 'Kojimachi', 'Nagatacho_Y': 'Nagatacho', 'Sakuradamon_Y': 'Sakuradamon',
        'Yurakucho_Y': 'Yurakucho', 'GinzaItchome_Y': 'Ginza-itchome', 'Shintomicho_Y': 'Shintomicho', 'Tsukishima_Y': 'Tsukishima',
        'Toyosu_Y': 'Toyosu', 'Tatsumi_Y': 'Tatsumi', 'ShinKiba_Y': 'Shinkiba',
        
        # Hanzomon Line (14 stations)
        'Shibuya_Z': 'Shibuya', 'Omotesando_Z': 'Omotesando', 'AoyamaItchome_Z': 'Aoyama-itchome', 'Nagatacho_Z': 'Nagatacho',
        'Hanzomon_Z': 'Hanzomon', 'Kudanshita_Z': 'Kudanshita', 'Jimbocho_Z': 'Jimbocho', 'Otemachi_Z': 'Otemachi',
        'Mitsukoshimae_Z': 'Mitsukoshimae', 'Suitengumae_Z': 'Suitengumae', 'KiyosumiShirakawa_Z': 'Kiyosumi-shirakawa', 'Sumiyoshi_Z': 'Sumiyoshi',
        'Kinshicho_Z': 'Kinshicho', 'Oshiage_Z': 'Oshiage',
        
        # Namboku Line (19 stations)
        'Meguro_N': 'Meguro', 'Shirokanedai_N': 'Shirokanedai', 'ShirokaneTakanawa_N': 'Shirokane-takanawa', 'AzabuJuban_N': 'Azabu-juban',
        'RoppongiItchome_N': 'Roppongi-itchome', 'TameikeSanno_N': 'Tameike-sanno', 'Nagatacho_N': 'Nagatacho', 'Yotsuya_N': 'Yotsuya',
        'Ichigaya_N': 'Ichigaya', 'Idabashi_N': 'Idabashi', 'Korakuen_N': 'Korakuen', 'Todaimae_N': 'Todaimae',
        'HonKomagome_N': 'Hon-komagome', 'Komagome_N': 'Komagome', 'Nishigahara_N': 'Nishigahara', 'Oji_N': 'Oji',
        'OjiKamiya_N': 'Oji-kamiya', 'Shimo_N': 'Shimo', 'AkabaneIwabuchi_N': 'Akabane-iwabuchi',
        
        # Fukutoshin Line (16 stations)
        'Wakoshi_F': 'Wakoshi', 'ChikatetsuAkatsuka_F': 'Chikatetsu-akatsuka', 'Heiwadai_F': 'Heiwadai', 'Hikawadai_F': 'Hikawadai',
        'KotakeMukaihara_F': 'Kotake-mukaihara', 'Senkawa_F': 'Senkawa', 'Kanamecho_F': 'Kanamecho', 'Ikebukuro_F': 'Ikebukuro',
        'Zoshigaya_F': 'Zoshigaya', 'NishiWaseda_F': 'Nishi-waseda', 'HigashiShinjuku_F': 'Higashi-shinjuku', 'ShinjukuSanchome_F': 'Shinjuku-sanchome',
        'Kitasando_F': 'Kitasando', 'MeijiJingumae_F': 'Meiji-jingumae', 'Shibuya_F': 'Shibuya',
        
        # Asakusa Line (20 stations)
        'NishiMagome_A': 'Nishi-magome', 'Magome_A': 'Magome', 'Nakanobu_A': 'Nakanobu', 'Togoshi_A': 'Togoshi', 'Gotanda_A': 'Gotanda',
        'Takanawadai_A': 'Takanawadai', 'Sengakuji_A': 'Sengakuji', 'Mita_A': 'Mita', 'Daimon_A': 'Daimon', 'Shimbashi_A': 'Shimbashi',
        'HigashiGinza_A': 'Higashi-ginza', 'Nihonbashi_A': 'Nihonbashi', 'Ningyocho_A': 'Ningyocho', 'HigashiNihonbashi_A': 'Higashi-nihonbashi',
        'Asakusabashi_A': 'Asakusabashi', 'Kuramae_A': 'Kuramae', 'Asakusa_A': 'Asakusa', 'HonjoAzumabashi_A': 'Honjo-azumabashi',
        'Oshiage_A': 'Oshiage',
        
        # Mita Line (27 stations)
        'NishiTakashimadaira_I': 'Nishi-takashimadaira', 'Takashimadaira_I': 'Takashimadaira', 'ShimuraSakaue_I': 'Shimura-sakaue', 'ShimuraSanchome_I': 'Shimura-sanchome',
        'Hasune_I': 'Hasune', 'Nishidai_I': 'Nishidai', 'TakashimadairaKoen_I': 'Takashimadaira-koen', 'ShinItabashi_I': 'Shin-itabashi', 'ItabashiKuyakushomae_I': 'Itabashi-kuyakushomae',
        'ItabashiHoncho_I': 'Itabashi-honcho', 'Motohasunuma_I': 'Motohasunuma', 'Shimura_I': 'Shimura', 'Nishigahara_I': 'Nishigahara', 'Oji_I': 'Oji',
        'OjiKamiya_I': 'Oji-kamiya', 'Shimo_I': 'Shimo', 'AkabaneIwabuchi_I': 'Akabane-iwabuchi', 'Sugamo_I': 'Sugamo', 'NishiSugamo_I': 'Nishi-sugamo',
        'ShinKoshinzuka_I': 'Shin-koshinzuka', 'HigashiIkebukuro_I': 'Higashi-ikebukuro', 'Kasuga_I': 'Kasuga', 'Hakusan_I': 'Hakusan', 'Sengoku_I': 'Sengoku',
        
        # Shinjuku Line (21 stations)
        'Motoyawata_S': 'Motoyawata', 'IchikawaShibayama_S': 'Ichikawa-shibayama', 'Funabori_S': 'Funabori', 'ShinKoiwa_S': 'Shin-koiwa', 'HigashiOjima_S': 'Higashi-ojima',
        'Ojima_S': 'Ojima', 'Sumiyoshi_S': 'Sumiyoshi', 'NishiOjima_S': 'Nishi-ojima', 'Kikukawa_S': 'Kikukawa', 'ShinOjima_S': 'Shin-ojima', 'Morishita_S': 'Morishita',
        'Hamacho_S': 'Hamacho', 'Bakuroyokoyama_S': 'Bakuroyokoyama', 'Iwamotocho_S': 'Iwamotocho', 'Ogawamachi_S': 'Ogawamachi', 'ShinOchanomizu_S': 'Shin-ochinomizu',
        'Jimbocho_S': 'Jimbocho', 'Kudanshita_S': 'Kudanshita', 'Ichigaya_S': 'Ichigaya', 'YotsuyaSanchome_S': 'Yotsuya-sanchome', 'Shinjuku_S': 'Shinjuku',
        
        # Oedo Line (38 stations)
        'TochoMae_E': 'Tocho-mae', 'ShinjukuNishiguchi_E': 'Shinjuku-nishiguchi', 'HigashiShinjuku_E': 'Higashi-shinjuku', 'WakamatsuKawada_E': 'Wakamatsu-kawada',
        'UshigomeYanagicho_E': 'Ushigome-yanagicho', 'UshigomeKagurazaka_E': 'Ushigome-kagurazaka', 'Iidabashi_E': 'Iidabashi', 'Kasuga_E': 'Kasuga',
        'Hongosanchome_E': 'Hongo-sanchome', 'UenoOkachimachi_E': 'Ueno-okachimachi', 'ShinOkachimachi_E': 'Shin-okachimachi', 'Kuramae_E': 'Kuramae',
        'Ryogoku_E': 'Ryogoku', 'Morishita_E': 'Morishita', 'KiyosumiShirakawa_E': 'Kiyosumi-shirakawa', 'MonzenNakacho_E': 'Monzen-nakacho',
        'Tsukishima_E': 'Tsukishima', 'Kachidoki_E': 'Kachidoki', 'Tsukijishijo_E': 'Tsukijishijo', 'Shiodome_E': 'Shiodome', 'Daimon_E': 'Daimon',
        'Akabanebashi_E': 'Akabanebashi', 'AzabuJuban_E': 'Azabu-juban', 'Roppongi_E': 'Roppongi', 'AoyamaItchome_E': 'Aoyama-itchome',
        'KokuritsuKyougijo_E': 'Kokuritsu-kyougijo', 'Yoyogi_E': 'Yoyogi', 'Shinjuku_E': 'Shinjuku', 'TochoMae_E': 'Tocho-mae'
    },
    'zh': {
        # 银座线 (19站)
        'Shibuya_G': '涩谷', 'Omotesando_G': '表参道', 'AoyamaItchome_G': '青山一丁目', 'Gaiemmae_G': '外苑前', 
        'AkasakaMitsuke_G': '赤坂见附', 'TameikeSanno_G': '溜池山王', 'Toranomon_G': '虎之门', 'Shimbashi_G': '新桥',
        'Ginza_G': '银座', 'Kyobashi_G': '京桥', 'Nihonbashi_G': '日本桥', 'Mitsukoshimae_G': '三越前',
        'Kanda_G': '神田', 'Suehirocho_G': '末广町', 'Uenohirokoji_G': '上野广小路', 'Ueno_G': '上野',
        'Inaricho_G': '稻荷町', 'Tawaramachi_G': '田原町', 'Asakusa_G': '浅草',
        
        # 丸之内线 (28站)
        'Ogikubo_M': '荻洼', 'MinamiAsagaya_M': '南阿佐谷', 'Shinkoenji_M': '新高圆寺', 'Higashikoenji_M': '东高圆寺',
        'ShinNakano_M': '新中野', 'NakanoFujimicho_M': '中野富士见町', 'NakanoShimbashi_M': '中野新桥', 'NakanoSakaue_M': '中野坂上',
        'NishiShinjuku_M': '西新宿', 'Shinjuku_M': '新宿', 'ShinjukuSanchome_M': '新宿三丁目', 'ShinjukuGyoemmae_M': '新宿御苑前',
        'YotsuyaSanchome_M': '四谷三丁目', 'Yotsuya_M': '四谷', 'AkasakaMitsuke_M': '赤坂见附', 'KokkaiGijidomae_M': '国会议事堂前',
        'Kasumigaseki_M': '霞关', 'Ginza_M': '银座', 'Tokyo_M': '东京', 'Otemachi_M': '大手町',
        'Awajicho_M': '淡路町', 'Ochanomizu_M': '御茶之水', 'Hongosanchome_M': '本乡三丁目', 'Korakuen_M': '后乐园',
        'Myogadani_M': '茗荷谷', 'Shinotsuka_M': '新大冢', 'Ikebukuro_M': '池袋',
        
        # 日比谷线 (21站)
        'NakaMeguro_H': '中目黑', 'Ebisu_H': '惠比寿', 'Hiroo_H': '广尾', 'Roppongi_H': '六本木',
        'Kamiyacho_H': '神谷町', 'Kasumigaseki_H': '霞关', 'Hibiya_H': '日比谷', 'Ginza_H': '银座',
        'HigashiGinza_H': '东银座', 'Tsukiji_H': '筑地', 'Hatchobori_H': '八丁堀', 'Kayabacho_H': '茅场町',
        'Nihonbashi_H': '日本桥', 'Mitsukoshimae_H': '三越前', 'Kanda_H': '神田', 'Akihabara_H': '秋叶原',
        'NakaOkachimachi_H': '仲御徒町', 'Ueno_H': '上野', 'Iriya_H': '入谷', 'Minowa_H': '三之轮',
        'MinamiSenju_H': '南千住', 'KitaSenju_H': '北千住',
        
        # 东西线 (23站)
        'Nakano_T': '中野', 'Ochiai_T': '落合', 'Takadanobaba_T': '高田马场', 'Waseda_T': '早稻田',
        'Kagurazaka_T': '神乐坂', 'Iidabashi_T': '饭田桥', 'Kudanshita_T': '九段下', 'Takebashi_T': '竹桥',
        'Otemachi_T': '大手町', 'Nihonbashi_T': '日本桥', 'Kayabacho_T': '茅场町', 'MonzenNakacho_T': '门前仲町',
        'Kiba_T': '木场', 'Toyocho_T': '丰洲', 'MinamiSunamachi_T': '南砂町', 'Shinkiba_T': '新木场',
        'NishiFunabashi_T': '西船桥', 'Funabashi_T': '船桥', 'Tsudanuma_T': '津田沼', 'Myoden_T': '妙典',
        'Barakinakayama_T': '原木中山', 'Hirai_T': '平井', 'Koiwa_T': '小岩',
        
        # 千代田线 (20站)
        'YoyogiUehara_C': '代代木上原', 'YoyogiKohen_C': '代代木公园', 'MeijiJingumae_C': '明治神宫前', 'Omotesando_C': '表参道',
        'Nogizaka_C': '乃木坂', 'Akasaka_C': '赤坂', 'KokkaiGijidomae_C': '国会议事堂前', 'Kasumigaseki_C': '霞关',
        'Hibiya_C': '日比谷', 'Nijubashimae_C': '二重桥前', 'Otemachi_C': '大手町', 'ShinOchanomizu_C': '新御茶之水',
        'Yushima_C': '汤岛', 'Nezu_C': '根津', 'Sendagi_C': '千驮木', 'NishiNippori_C': '西日暮里',
        'Machiya_C': '町屋', 'KitaSenju_C': '北千住', 'Ayase_C': '绫濑',
        
        # 有乐町线 (24站)
        'Wakoshi_Y': '和光市', 'ChikatetsuAkatsuka_Y': '地铁赤冢', 'Heiwadai_Y': '平和台', 'Hikawadai_Y': '冰川台',
        'KotakeMukaihara_Y': '小竹向原', 'Senkawa_Y': '千川', 'Kanamecho_Y': '要町', 'Ikebukuro_Y': '池袋',
        'HigashiIkebukuro_Y': '东池袋', 'Gokokuji_Y': '护国寺', 'Edogawabashi_Y': '江户川桥', 'Iidabashi_Y': '饭田桥',
        'Ichigaya_Y': '市谷', 'Kojimachi_Y': '麹町', 'Nagatacho_Y': '永田町', 'Sakuradamon_Y': '樱田门',
        'Yurakucho_Y': '有乐町', 'GinzaItchome_Y': '银座一丁目', 'Shintomicho_Y': '新富町', 'Tsukishima_Y': '月岛',
        'Toyosu_Y': '丰洲', 'Tatsumi_Y': '辰巳', 'ShinKiba_Y': '新木场',
        
        # 半藏门线 (14站)
        'Shibuya_Z': '涩谷', 'Omotesando_Z': '表参道', 'AoyamaItchome_Z': '青山一丁目', 'Nagatacho_Z': '永田町',
        'Hanzomon_Z': '半藏门', 'Kudanshita_Z': '九段下', 'Jimbocho_Z': '神保町', 'Otemachi_Z': '大手町',
        'Mitsukoshimae_Z': '三越前', 'Suitengumae_Z': '水天宫前', 'KiyosumiShirakawa_Z': '清澄白河', 'Sumiyoshi_Z': '住吉',
        'Kinshicho_Z': '锦系町', 'Oshiage_Z': '押上',
        
        # 南北线 (19站)
        'Meguro_N': '目黑', 'Shirokanedai_N': '白金台', 'ShirokaneTakanawa_N': '白金高轮', 'AzabuJuban_N': '麻布十番',
        'RoppongiItchome_N': '六本木一丁目', 'TameikeSanno_N': '溜池山王', 'Nagatacho_N': '永田町', 'Yotsuya_N': '四谷',
        'Ichigaya_N': '市谷', 'Idabashi_N': '饭田桥', 'Korakuen_N': '后乐园', 'Todaimae_N': '东大前',
        'HonKomagome_N': '本驹込', 'Komagome_N': '驹込', 'Nishigahara_N': '西原', 'Oji_N': '王子',
        'OjiKamiya_N': '王子神谷', 'Shimo_N': '志茂', 'AkabaneIwabuchi_N': '赤羽岩渊',
        
        # 副都心线 (16站)
        'Wakoshi_F': '和光市', 'ChikatetsuAkatsuka_F': '地铁赤冢', 'Heiwadai_F': '平和台', 'Hikawadai_F': '冰川台',
        'KotakeMukaihara_F': '小竹向原', 'Senkawa_F': '千川', 'Kanamecho_F': '要町', 'Ikebukuro_F': '池袋',
        'Zoshigaya_F': '杂司谷', 'NishiWaseda_F': '西早稻田', 'HigashiShinjuku_F': '东新宿', 'ShinjukuSanchome_F': '新宿三丁目',
        'Kitasando_F': '北参道', 'MeijiJingumae_F': '明治神宫前', 'Shibuya_F': '涩谷',
        
        # 浅草线 (20站)
        'NishiMagome_A': '西马込', 'Magome_A': '马込', 'Nakanobu_A': '中延', 'Togoshi_A': '户越', 'Gotanda_A': '五反田',
        'Takanawadai_A': '高轮台', 'Sengakuji_A': '泉岳寺', 'Mita_A': '三田', 'Daimon_A': '大门', 'Shimbashi_A': '新桥',
        'HigashiGinza_A': '东银座', 'Nihonbashi_A': '日本桥', 'Ningyocho_A': '人形町', 'HigashiNihonbashi_A': '东日本桥',
        'Asakusabashi_A': '浅草桥', 'Kuramae_A': '藏前', 'Asakusa_A': '浅草', 'HonjoAzumabashi_A': '本所吾妻桥',
        'Oshiage_A': '押上',
        
        # 三田线 (27站)
        'NishiTakashimadaira_I': '西高岛平', 'Takashimadaira_I': '高岛平', 'ShimuraSakaue_I': '志村坂上', 'ShimuraSanchome_I': '志村三丁目',
        'Hasune_I': '莲根', 'Nishidai_I': '西台', 'TakashimadairaKoen_I': '高岛平公园', 'ShinItabashi_I': '新板桥', 'ItabashiKuyakushomae_I': '板桥区役所前',
        'ItabashiHoncho_I': '板桥本町', 'Motohasunuma_I': '本莲沼', 'Shimura_I': '志村', 'Nishigahara_I': '西原', 'Oji_I': '王子',
        'OjiKamiya_I': '王子神谷', 'Shimo_I': '志茂', 'AkabaneIwabuchi_I': '赤羽岩渊', 'Sugamo_I': '巢鸭', 'NishiSugamo_I': '西巢鸭',
        'ShinKoshinzuka_I': '新庚申冢', 'HigashiIkebukuro_I': '东池袋', 'Kasuga_I': '春日', 'Hakusan_I': '白山', 'Sengoku_I': '千石',
        
        # 新宿线 (21站)
        'Motoyawata_S': '本八幡', 'IchikawaShibayama_S': '市川盐滨', 'Funabori_S': '船堀', 'ShinKoiwa_S': '新小岩', 'HigashiOjima_S': '东大岛',
        'Ojima_S': '大岛', 'Sumiyoshi_S': '住吉', 'NishiOjima_S': '西大岛', 'Kikukawa_S': '菊川', 'ShinOjima_S': '新大岛', 'Morishita_S': '森下',
        'Hamacho_S': '滨町', 'Bakuroyokoyama_S': '马喰横山', 'Iwamotocho_S': '岩本町', 'Ogawamachi_S': '小川町', 'ShinOchanomizu_S': '新御茶之水',
        'Jimbocho_S': '神保町', 'Kudanshita_S': '九段下', 'Ichigaya_S': '市谷', 'YotsuyaSanchome_S': '四谷三丁目', 'Shinjuku_S': '新宿',
        
        # 大江户线 (38站)
        'TochoMae_E': '都厅前', 'ShinjukuNishiguchi_E': '新宿西口', 'HigashiShinjuku_E': '东新宿', 'WakamatsuKawada_E': '若松河田',
        'UshigomeYanagicho_E': '牛込柳町', 'UshigomeKagurazaka_E': '牛込神乐坂', 'Iidabashi_E': '饭田桥', 'Kasuga_E': '春日',
        'Hongosanchome_E': '本乡三丁目', 'UenoOkachimachi_E': '上野御徒町', 'ShinOkachimachi_E': '新御徒町', 'Kuramae_E': '藏前',
        'Ryogoku_E': '两国', 'Morishita_E': '森下', 'KiyosumiShirakawa_E': '清澄白河', 'MonzenNakacho_E': '门前仲町',
        'Tsukishima_E': '月岛', 'Kachidoki_E': '胜鬨', 'Tsukijishijo_E': '筑地市场', 'Shiodome_E': '汐留', 'Daimon_E': '大门',
        'Akabanebashi_E': '赤羽桥', 'AzabuJuban_E': '麻布十番', 'Roppongi_E': '六本木', 'AoyamaItchome_E': '青山一丁目',
        'KokuritsuKyougijo_E': '国立竞技场', 'Yoyogi_E': '代代木', 'Shinjuku_E': '新宿', 'TochoMae_E': '都厅前'
    }
}

# 地铁线路连接关系（车站间的距离，单位：分钟）
SUBWAY_CONNECTIONS = [
    # 银座线 (18个连接)
    ('Shibuya_G', 'Omotesando_G', 2),
    ('Omotesando_G', 'AoyamaItchome_G', 2),
    ('AoyamaItchome_G', 'Gaiemmae_G', 1),
    ('Gaiemmae_G', 'AkasakaMitsuke_G', 2),
    ('AkasakaMitsuke_G', 'TameikeSanno_G', 1),
    ('TameikeSanno_G', 'Toranomon_G', 1),
    ('Toranomon_G', 'Shimbashi_G', 2),
    ('Shimbashi_G', 'Ginza_G', 1),
    ('Ginza_G', 'Kyobashi_G', 1),
    ('Kyobashi_G', 'Nihonbashi_G', 1),
    ('Nihonbashi_G', 'Mitsukoshimae_G', 1),
    ('Mitsukoshimae_G', 'Kanda_G', 1),
    ('Kanda_G', 'Suehirocho_G', 2),
    ('Suehirocho_G', 'Uenohirokoji_G', 1),
    ('Uenohirokoji_G', 'Ueno_G', 1),
    ('Ueno_G', 'Inaricho_G', 1),
    ('Inaricho_G', 'Tawaramachi_G', 1),
    ('Tawaramachi_G', 'Asakusa_G', 1),
    
    # 丸之内线 (27个连接)
    ('Ogikubo_M', 'MinamiAsagaya_M', 2),
    ('MinamiAsagaya_M', 'Shinkoenji_M', 2),
    ('Shinkoenji_M', 'Higashikoenji_M', 1),
    ('Higashikoenji_M', 'ShinNakano_M', 1),
    ('ShinNakano_M', 'NakanoFujimicho_M', 1),
    ('NakanoFujimicho_M', 'NakanoShimbashi_M', 1),
    ('NakanoShimbashi_M', 'NakanoSakaue_M', 1),
    ('NakanoSakaue_M', 'NishiShinjuku_M', 2),
    ('NishiShinjuku_M', 'Shinjuku_M', 1),
    ('Shinjuku_M', 'ShinjukuSanchome_M', 1),
    ('ShinjukuSanchome_M', 'ShinjukuGyoemmae_M', 1),
    ('ShinjukuGyoemmae_M', 'YotsuyaSanchome_M', 1),
    ('YotsuyaSanchome_M', 'Yotsuya_M', 1),
    ('Yotsuya_M', 'AkasakaMitsuke_M', 2),
    ('AkasakaMitsuke_M', 'KokkaiGijidomae_M', 1),
    ('KokkaiGijidomae_M', 'Kasumigaseki_M', 1),
    ('Kasumigaseki_M', 'Ginza_M', 2),
    ('Ginza_M', 'Tokyo_M', 1),
    ('Tokyo_M', 'Otemachi_M', 1),
    ('Otemachi_M', 'Awajicho_M', 1),
    ('Awajicho_M', 'Ochanomizu_M', 1),
    ('Ochanomizu_M', 'Hongosanchome_M', 1),
    ('Hongosanchome_M', 'Korakuen_M', 1),
    ('Korakuen_M', 'Myogadani_M', 1),
    ('Myogadani_M', 'Shinotsuka_M', 1),
    ('Shinotsuka_M', 'Ikebukuro_M', 1),
    
    # 日比谷线 (20个连接)
    ('NakaMeguro_H', 'Ebisu_H', 1),
    ('Ebisu_H', 'Hiroo_H', 1),
    ('Hiroo_H', 'Roppongi_H', 2),
    ('Roppongi_H', 'Kamiyacho_H', 1),
    ('Kamiyacho_H', 'Kasumigaseki_H', 1),
    ('Kasumigaseki_H', 'Hibiya_H', 1),
    ('Hibiya_H', 'Ginza_H', 1),
    ('Ginza_H', 'HigashiGinza_H', 1),
    ('HigashiGinza_H', 'Tsukiji_H', 1),
    ('Tsukiji_H', 'Hatchobori_H', 1),
    ('Hatchobori_H', 'Kayabacho_H', 1),
    ('Kayabacho_H', 'Nihonbashi_H', 1),
    ('Nihonbashi_H', 'Mitsukoshimae_H', 1),
    ('Mitsukoshimae_H', 'Kanda_H', 1),
    ('Kanda_H', 'Akihabara_H', 1),
    ('Akihabara_H', 'NakaOkachimachi_H', 1),
    ('NakaOkachimachi_H', 'Ueno_H', 1),
    ('Ueno_H', 'Iriya_H', 1),
    ('Iriya_H', 'Minowa_H', 1),
    ('Minowa_H', 'MinamiSenju_H', 2),
    ('MinamiSenju_H', 'KitaSenju_H', 1),
    
    # 东西线 (22个连接)
    ('Nakano_T', 'Ochiai_T', 1),
    ('Ochiai_T', 'Takadanobaba_T', 2),
    ('Takadanobaba_T', 'Waseda_T', 1),
    ('Waseda_T', 'Kagurazaka_T', 1),
    ('Kagurazaka_T', 'Iidabashi_T', 1),
    ('Iidabashi_T', 'Kudanshita_T', 1),
    ('Kudanshita_T', 'Takebashi_T', 1),
    ('Takebashi_T', 'Otemachi_T', 1),
    ('Otemachi_T', 'Nihonbashi_T', 1),
    ('Nihonbashi_T', 'Kayabacho_T', 1),
    ('Kayabacho_T', 'MonzenNakacho_T', 1),
    ('MonzenNakacho_T', 'Kiba_T', 1),
    ('Kiba_T', 'Toyocho_T', 2),
    ('Toyocho_T', 'MinamiSunamachi_T', 1),
    ('MinamiSunamachi_T', 'Shinkiba_T', 2),
    ('Shinkiba_T', 'NishiFunabashi_T', 1),
    ('NishiFunabashi_T', 'Funabashi_T', 1),
    ('Funabashi_T', 'Tsudanuma_T', 1),
    ('Tsudanuma_T', 'Myoden_T', 1),
    ('Myoden_T', 'Barakinakayama_T', 1),
    ('Barakinakayama_T', 'Hirai_T', 1),
    ('Hirai_T', 'Koiwa_T', 1),
    
    # 千代田线 (19个连接)
    ('YoyogiUehara_C', 'YoyogiKohen_C', 1),
    ('YoyogiKohen_C', 'MeijiJingumae_C', 1),
    ('MeijiJingumae_C', 'Omotesando_C', 1),
    ('Omotesando_C', 'Nogizaka_C', 1),
    ('Nogizaka_C', 'Akasaka_C', 1),
    ('Akasaka_C', 'KokkaiGijidomae_C', 1),
    ('KokkaiGijidomae_C', 'Kasumigaseki_C', 1),
    ('Kasumigaseki_C', 'Hibiya_C', 1),
    ('Hibiya_C', 'Nijubashimae_C', 1),
    ('Nijubashimae_C', 'Otemachi_C', 1),
    ('Otemachi_C', 'ShinOchanomizu_C', 1),
    ('ShinOchanomizu_C', 'Yushima_C', 1),
    ('Yushima_C', 'Nezu_C', 1),
    ('Nezu_C', 'Sendagi_C', 1),
    ('Sendagi_C', 'NishiNippori_C', 1),
    ('NishiNippori_C', 'Machiya_C', 1),
    ('Machiya_C', 'KitaSenju_C', 2),
    ('KitaSenju_C', 'Ayase_C', 1),
    
    # 有乐町线 (23个连接)
    ('Wakoshi_Y', 'ChikatetsuAkatsuka_Y', 1),
    ('ChikatetsuAkatsuka_Y', 'Heiwadai_Y', 1),
    ('Heiwadai_Y', 'Hikawadai_Y', 1),
    ('Hikawadai_Y', 'KotakeMukaihara_Y', 1),
    ('KotakeMukaihara_Y', 'Senkawa_Y', 1),
    ('Senkawa_Y', 'Kanamecho_Y', 1),
    ('Kanamecho_Y', 'Ikebukuro_Y', 1),
    ('Ikebukuro_Y', 'HigashiIkebukuro_Y', 1),
    ('HigashiIkebukuro_Y', 'Gokokuji_Y', 1),
    ('Gokokuji_Y', 'Edogawabashi_Y', 1),
    ('Edogawabashi_Y', 'Iidabashi_Y', 1),
    ('Iidabashi_Y', 'Ichigaya_Y', 1),
    ('Ichigaya_Y', 'Kojimachi_Y', 1),
    ('Kojimachi_Y', 'Nagatacho_Y', 1),
    ('Nagatacho_Y', 'Sakuradamon_Y', 1),
    ('Sakuradamon_Y', 'Yurakucho_Y', 1),
    ('Yurakucho_Y', 'GinzaItchome_Y', 1),
    ('GinzaItchome_Y', 'Shintomicho_Y', 1),
    ('Shintomicho_Y', 'Tsukishima_Y', 1),
    ('Tsukishima_Y', 'Toyosu_Y', 1),
    ('Toyosu_Y', 'Tatsumi_Y', 1),
    ('Tatsumi_Y', 'ShinKiba_Y', 1),
    
    # 半藏门线 (13个连接)
    ('Shibuya_Z', 'Omotesando_Z', 1),
    ('Omotesando_Z', 'AoyamaItchome_Z', 1),
    ('AoyamaItchome_Z', 'Nagatacho_Z', 1),
    ('Nagatacho_Z', 'Hanzomon_Z', 1),
    ('Hanzomon_Z', 'Kudanshita_Z', 1),
    ('Kudanshita_Z', 'Jimbocho_Z', 1),
    ('Jimbocho_Z', 'Otemachi_Z', 1),
    ('Otemachi_Z', 'Mitsukoshimae_Z', 1),
    ('Mitsukoshimae_Z', 'Suitengumae_Z', 1),
    ('Suitengumae_Z', 'KiyosumiShirakawa_Z', 1),
    ('KiyosumiShirakawa_Z', 'Sumiyoshi_Z', 1),
    ('Sumiyoshi_Z', 'Kinshicho_Z', 1),
    ('Kinshicho_Z', 'Oshiage_Z', 1),
    
    # 南北线 (18个连接)
    ('Meguro_N', 'Shirokanedai_N', 1),
    ('Shirokanedai_N', 'ShirokaneTakanawa_N', 1),
    ('ShirokaneTakanawa_N', 'AzabuJuban_N', 1),
    ('AzabuJuban_N', 'RoppongiItchome_N', 1),
    ('RoppongiItchome_N', 'TameikeSanno_N', 1),
    ('TameikeSanno_N', 'Nagatacho_N', 1),
    ('Nagatacho_N', 'Yotsuya_N', 1),
    ('Yotsuya_N', 'Ichigaya_N', 1),
    ('Ichigaya_N', 'Idabashi_N', 1),
    ('Idabashi_N', 'Korakuen_N', 1),
    ('Korakuen_N', 'Todaimae_N', 1),
    ('Todaimae_N', 'HonKomagome_N', 1),
    ('HonKomagome_N', 'Komagome_N', 1),
    ('Komagome_N', 'Nishigahara_N', 1),
    ('Nishigahara_N', 'Oji_N', 1),
    ('Oji_N', 'OjiKamiya_N', 1),
    ('OjiKamiya_N', 'Shimo_N', 1),
    ('Shimo_N', 'AkabaneIwabuchi_N', 1),
    
    # 副都心线 (15个连接)
    ('Wakoshi_F', 'ChikatetsuAkatsuka_F', 1),
    ('ChikatetsuAkatsuka_F', 'Heiwadai_F', 1),
    ('Heiwadai_F', 'Hikawadai_F', 1),
    ('Hikawadai_F', 'KotakeMukaihara_F', 1),
    ('KotakeMukaihara_F', 'Senkawa_F', 1),
    ('Senkawa_F', 'Kanamecho_F', 1),
    ('Kanamecho_F', 'Ikebukuro_F', 1),
    ('Ikebukuro_F', 'Zoshigaya_F', 1),
    ('Zoshigaya_F', 'NishiWaseda_F', 1),
    ('NishiWaseda_F', 'HigashiShinjuku_F', 1),
    ('HigashiShinjuku_F', 'ShinjukuSanchome_F', 1),
    ('ShinjukuSanchome_F', 'Kitasando_F', 1),
    ('Kitasando_F', 'MeijiJingumae_F', 1),
    ('MeijiJingumae_F', 'Shibuya_F', 1),
    
    # 浅草线 (19个连接)
    ('NishiMagome_A', 'Magome_A', 2), ('Magome_A', 'Nakanobu_A', 1), ('Nakanobu_A', 'Togoshi_A', 1),
    ('Togoshi_A', 'Gotanda_A', 2), ('Gotanda_A', 'Takanawadai_A', 1), ('Takanawadai_A', 'Sengakuji_A', 1),
    ('Sengakuji_A', 'Mita_A', 1), ('Mita_A', 'Daimon_A', 1), ('Daimon_A', 'Shimbashi_A', 2),
    ('Shimbashi_A', 'HigashiGinza_A', 1), ('HigashiGinza_A', 'Nihonbashi_A', 1), ('Nihonbashi_A', 'Ningyocho_A', 1),
    ('Ningyocho_A', 'HigashiNihonbashi_A', 1), ('HigashiNihonbashi_A', 'Asakusabashi_A', 1), ('Asakusabashi_A', 'Kuramae_A', 1),
    ('Kuramae_A', 'Asakusa_A', 1), ('Asakusa_A', 'HonjoAzumabashi_A', 1), ('HonjoAzumabashi_A', 'Oshiage_A', 1),
    
    # 三田线 (26个连接)
    ('NishiTakashimadaira_I', 'Takashimadaira_I', 1), ('Takashimadaira_I', 'ShimuraSakaue_I', 1), ('ShimuraSakaue_I', 'ShimuraSanchome_I', 1),
    ('ShimuraSanchome_I', 'Hasune_I', 1), ('Hasune_I', 'Nishidai_I', 1), ('Nishidai_I', 'TakashimadairaKoen_I', 1),
    ('TakashimadairaKoen_I', 'ShinItabashi_I', 1), ('ShinItabashi_I', 'ItabashiKuyakushomae_I', 1), ('ItabashiKuyakushomae_I', 'ItabashiHoncho_I', 1),
    ('ItabashiHoncho_I', 'Motohasunuma_I', 1), ('Motohasunuma_I', 'Shimura_I', 1), ('Shimura_I', 'Nishigahara_I', 1),
    ('Nishigahara_I', 'Oji_I', 1), ('Oji_I', 'OjiKamiya_I', 1), ('OjiKamiya_I', 'Shimo_I', 1),
    ('Shimo_I', 'AkabaneIwabuchi_I', 1), ('AkabaneIwabuchi_I', 'Sugamo_I', 1), ('Sugamo_I', 'NishiSugamo_I', 1),
    ('NishiSugamo_I', 'ShinKoshinzuka_I', 1), ('ShinKoshinzuka_I', 'HigashiIkebukuro_I', 1), ('HigashiIkebukuro_I', 'Kasuga_I', 1),
    ('Kasuga_I', 'Hakusan_I', 1), ('Hakusan_I', 'Sengoku_I', 1),
    
    # 新宿线 (20个连接)
    ('Motoyawata_S', 'IchikawaShibayama_S', 1), ('IchikawaShibayama_S', 'Funabori_S', 1), ('Funabori_S', 'ShinKoiwa_S', 1),
    ('ShinKoiwa_S', 'HigashiOjima_S', 1), ('HigashiOjima_S', 'Ojima_S', 1), ('Ojima_S', 'Sumiyoshi_S', 1),
    ('Sumiyoshi_S', 'NishiOjima_S', 1), ('NishiOjima_S', 'Kikukawa_S', 1), ('Kikukawa_S', 'ShinOjima_S', 1),
    ('ShinOjima_S', 'Morishita_S', 1), ('Morishita_S', 'Hamacho_S', 1), ('Hamacho_S', 'Bakuroyokoyama_S', 1),
    ('Bakuroyokoyama_S', 'Iwamotocho_S', 1), ('Iwamotocho_S', 'Ogawamachi_S', 1), ('Ogawamachi_S', 'ShinOchanomizu_S', 1),
    ('ShinOchanomizu_S', 'Jimbocho_S', 1), ('Jimbocho_S', 'Kudanshita_S', 1), ('Kudanshita_S', 'Ichigaya_S', 1),
    ('Ichigaya_S', 'YotsuyaSanchome_S', 1), ('YotsuyaSanchome_S', 'Shinjuku_S', 1),
    
    # 大江户线 (37个连接)
    ('TochoMae_E', 'ShinjukuNishiguchi_E', 1), ('ShinjukuNishiguchi_E', 'HigashiShinjuku_E', 1), ('HigashiShinjuku_E', 'WakamatsuKawada_E', 1),
    ('WakamatsuKawada_E', 'UshigomeYanagicho_E', 1), ('UshigomeYanagicho_E', 'UshigomeKagurazaka_E', 1), ('UshigomeKagurazaka_E', 'Iidabashi_E', 1),
    ('Iidabashi_E', 'Kasuga_E', 1), ('Kasuga_E', 'Hongosanchome_E', 1), ('Hongosanchome_E', 'UenoOkachimachi_E', 1),
    ('UenoOkachimachi_E', 'ShinOkachimachi_E', 1), ('ShinOkachimachi_E', 'Kuramae_E', 1), ('Kuramae_E', 'Ryogoku_E', 1),
    ('Ryogoku_E', 'Morishita_E', 1), ('Morishita_E', 'KiyosumiShirakawa_E', 1), ('KiyosumiShirakawa_E', 'MonzenNakacho_E', 1),
    ('MonzenNakacho_E', 'Tsukishima_E', 1), ('Tsukishima_E', 'Kachidoki_E', 1), ('Kachidoki_E', 'Tsukijishijo_E', 1),
    ('Tsukijishijo_E', 'Shiodome_E', 1), ('Shiodome_E', 'Daimon_E', 1), ('Daimon_E', 'Akabanebashi_E', 1),
    ('Akabanebashi_E', 'AzabuJuban_E', 1), ('AzabuJuban_E', 'Roppongi_E', 1), ('Roppongi_E', 'AoyamaItchome_E', 1),
    ('AoyamaItchome_E', 'KokuritsuKyougijo_E', 1), ('KokuritsuKyougijo_E', 'Yoyogi_E', 1), ('Yoyogi_E', 'Shinjuku_E', 1),
    ('Shinjuku_E', 'TochoMae_E', 1),
    
    # 换乘站连接（相同车站的不同线路）
    ('Shibuya_G', 'Shibuya_M', 1),
    ('Shibuya_G', 'Shibuya_Z', 1),
    ('Shibuya_M', 'Shibuya_Z', 1),
    ('Shibuya_G', 'Shibuya_F', 1),
    ('Shibuya_M', 'Shibuya_F', 1),
    ('Shibuya_Z', 'Shibuya_F', 1),
    ('Ginza_G', 'Ginza_H', 1),
    ('Ginza_G', 'Ginza_M', 1),
    ('Ueno_G', 'Ueno_H', 1),
    ('Ikebukuro_M', 'Ikebukuro_Y', 1),
    ('Ikebukuro_M', 'Ikebukuro_F', 1),
    ('Ikebukuro_Y', 'Ikebukuro_F', 1),
    ('Otemachi_M', 'Otemachi_T', 1),
    ('Otemachi_M', 'Otemachi_N', 1),
    ('Otemachi_M', 'Otemachi_C', 1),
    ('Otemachi_T', 'Otemachi_N', 1),
    ('Otemachi_T', 'Otemachi_C', 1),
    ('Otemachi_N', 'Otemachi_C', 1),
    ('AkasakaMitsuke_G', 'AkasakaMitsuke_M', 1),
    ('AkasakaMitsuke_G', 'AkasakaMitsuke_H', 1),
    ('AkasakaMitsuke_M', 'AkasakaMitsuke_H', 1),
    ('Nagatacho_Z', 'Nagatacho_N', 1),
    ('Nagatacho_Z', 'Nagatacho_Y', 1),
    ('Nagatacho_N', 'Nagatacho_Y', 1),
    ('Iidabashi_T', 'Iidabashi_Y', 1),
    ('Iidabashi_T', 'Iidabashi_N', 1),
    ('Iidabashi_Y', 'Iidabashi_N', 1),
    
    # 新增的4条都营地铁线路换乘连接
    ('Asakusa_G', 'Asakusa_A', 1),
    ('Oshiage_Z', 'Oshiage_A', 1),
    ('Mita_I', 'Mita_A', 1),
    ('Shimbashi_A', 'Shimbashi_G', 1),
    ('Shimbashi_A', 'Shimbashi_H', 1),
    ('Nihonbashi_A', 'Nihonbashi_G', 1),
    ('Nihonbashi_A', 'Nihonbashi_H', 1),
    ('Nihonbashi_A', 'Nihonbashi_T', 1),
    ('Kuramae_A', 'Kuramae_E', 1),
    ('Shinjuku_S', 'Shinjuku_M', 1),
    ('Shinjuku_S', 'Shinjuku_F', 1),
    ('Shinjuku_S', 'Shinjuku_E', 1),
    ('Ichigaya_S', 'Ichigaya_N', 1),
    ('Ichigaya_S', 'Ichigaya_Y', 1),
    ('Kudanshita_S', 'Kudanshita_Z', 1),
    ('Jimbocho_S', 'Jimbocho_Z', 1),
    ('Iidabashi_E', 'Iidabashi_T', 1),
    ('Iidabashi_E', 'Iidabashi_Y', 1),
    ('Kasuga_E', 'Kasuga_I', 1),
    ('Hongosanchome_E', 'Hongosanchome_M', 1),
    ('Kuramae_E', 'Kuramae_A', 1),
    ('Morishita_E', 'Morishita_S', 1),
    ('KiyosumiShirakawa_E', 'KiyosumiShirakawa_Z', 1),
    ('MonzenNakacho_E', 'MonzenNakacho_T', 1),
    ('Tsukishima_E', 'Tsukishima_Y', 1),
    ('Daimon_E', 'Daimon_A', 1),
    ('Akabanebashi_E', 'Akabanebashi_H', 1),
    ('AzabuJuban_E', 'AzabuJuban_N', 1),
    ('Roppongi_E', 'Roppongi_H', 1),
    ('AoyamaItchome_E', 'AoyamaItchome_G', 1),
    ('AoyamaItchome_E', 'AoyamaItchome_Z', 1),
    ('Yoyogi_E', 'Yoyogi_C', 1)
]

# 获取所有车站的唯一标识符
def get_all_station_ids():
    """获取所有车站的唯一ID"""
    return list(set([conn[0] for conn in SUBWAY_CONNECTIONS] + [conn[1] for conn in SUBWAY_CONNECTIONS]))

# 获取车站名称（根据语言）
def get_station_name(station_id, lang='ja'):
    """根据车站ID和语言获取车站名称"""
    return TOKYO_SUBWAY_STATIONS.get(lang, {}).get(station_id, station_id)

# 获取线路名称（根据语言）
def get_line_name(line_code, lang='ja'):
    """根据线路代码和语言获取线路名称"""
    return TOKYO_SUBWAY_LINES.get(lang, {}).get(line_code, line_code)

# 获取车站所在的线路
def get_station_lines(station_id):
    """获取车站所在的线路代码"""
    lines = []
    for line_code in TOKYO_SUBWAY_LINES['ja'].keys():
        if station_id.endswith('_' + line_code):
            lines.append(line_code)
    return lines

# 获取线路的车站顺序
def get_line_station_order(line_code):
    """获取特定线路的车站运行顺序"""
    # 构建线路的车站连接图
    line_connections = {}
    
    # 找出该线路的所有连接
    for connection in SUBWAY_CONNECTIONS:
        station1, station2, time = connection
        
        # 检查两个车站是否都在该线路上
        if line_code in get_station_lines(station1) and line_code in get_station_lines(station2):
            if station1 not in line_connections:
                line_connections[station1] = []
            if station2 not in line_connections:
                line_connections[station2] = []
            
            line_connections[station1].append((station2, time))
            line_connections[station2].append((station1, time))
    
    if not line_connections:
        return []
    
    # 找到起点（度数为1的车站）
    start_stations = [station for station, connections in line_connections.items() 
                     if len(connections) == 1]
    
    if not start_stations:
        # 如果是环形线路，任意选择一个起点
        start_station = list(line_connections.keys())[0]
    else:
        start_station = start_stations[0]
    
    # 使用深度优先搜索确定车站顺序
    visited = set()
    station_order = []
    
    def dfs(current_station):
        visited.add(current_station)
        station_order.append(current_station)
        
        for neighbor, _ in line_connections.get(current_station, []):
            if neighbor not in visited:
                dfs(neighbor)
    
    dfs(start_station)
    return station_order

# 构建图结构
def build_subway_graph():
    """构建地铁图的邻接表表示"""
    graph = {}
    
    # 初始化所有车站
    for station_id in get_all_station_ids():
        graph[station_id] = {}
    
    # 添加连接关系
    for connection in SUBWAY_CONNECTIONS:
        station1, station2, time = connection
        graph[station1][station2] = time
        graph[station2][station1] = time
    
    return graph

if __name__ == "__main__":
    # 测试数据
    graph = build_subway_graph()
    print("地铁图构建完成，包含车站数量:", len(graph))
    print("示例车站连接:")
    for station, connections in list(graph.items())[:3]:
        print(f"{station}: {connections}")