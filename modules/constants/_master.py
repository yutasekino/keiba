import dataclasses
from types import MappingProxyType

@dataclasses.dataclass(frozen=True)
class Master:
    PLACE_DICT: dict = MappingProxyType({
        '札幌':'01',
        '函館':'02',
        '福島':'03',
        '新潟':'04',
        '東京':'05',
        '中山':'06',
        '中京':'07',
        '京都':'08',
        '阪神':'09',
        '小倉':'10',
        '門別':'30',
        '旭川':'34',
        '盛岡':'35',
        '水沢':'36',
        '浦和':'42',
        '船橋':'43',
        '大井':'44',
        '川崎':'45',
        '金沢':'46',
        '笠松':'47',
        '名古屋':'48',
        '園田':'50',
        '姫路':'51',
        '福山':'53',
        '高知':'54',
        '佐賀':'55',
        '荒尾':'56',
        '札幌(地)':'58',
        '香港':'60',
        'フランス':'61',
        'オースト':'62',
        'イギリス':'63',
        'シャティ':'64',
        'アラブ首':'65',
        'メイダン':'66',
        'ドイツ':'67',
        'アイルラ':'68',
        'アメリカ':'69',
        'ロンシャ':'70',
        'イタリア':'71',
        'シンガポ':'72',
        'カナダ':'73',
        'シャンテ':'74',
        '韓国':'75',
        'フレミン':'76',
        'ニュージ':'77',
        'アスコッ':'78',
        'デルマー':'79',
        'サンタア':'80',
        'コーフィ':'81',
        'ベルモン':'82',
        'ドーヴィ':'83',
        'ランドウ':'84',
        'ヨーク':'85',
        'レパーズ':'86',
        'チャーチ':'87',
        'サンダウ':'88'
        })

    RACE_TYPE_DICT: dict = MappingProxyType({
        '芝': '芝',
        'ダ': 'ダート',
        '障': '障害',
        })
    
    WEATHER_LIST: tuple = ('晴', '曇', '小雨', '雨', '小雪', '雪')
    
    GROUND_STATE_LIST: tuple = ('良', '稍重', '重', '不良')
    
    SEX_LIST: tuple = ('牡', '牝', 'セ')
    
    AROUND_LIST: tuple = ('右', '左', '直線', '障害')

    RACE_CLASS_LIST: tuple = ('新馬', '未勝利', '1勝クラス', '2勝クラス', '3勝クラス', 'オープン', 'G3', 'G2', 'G1', '障害')