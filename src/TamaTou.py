# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura (https://github.com/hirmiura)
#
# TamaTouを生成するスクリプト
#
# 使い方
# 1. fontforgeでコンソールを出す(fontforge-console.bat)
# 2. ディレクトリ移動
# 3. ffpython TamaTou.py
# 4. 待つ
#
# Orbitron → オービトロン → オーブ → 玉 → Tamaやな！
# Noto → No Toufu → 豆腐だらけだし → Touやな！
#     →→ TamaTou
#
import fontforge

for weight in ['Regular', 'Bold']:

    print('玉改変')
    fn = fontforge.open(f'Orbitron-{weight}.ttf')
    fn.encoding = 'UnicodeFull'
    fn.save(f'tmp1-{weight}.sfd')
    fn.close()

    print(f'能登改変 {weight}')
    fn = fontforge.open(f'NotoSansJP-{weight}.otf')
    fn.encoding = 'UnicodeFull'
    fn.cidFlatten()
    # fn.ascent = 800
    # fn.descent = 200
    # fn.upos = -125
    # fn.em = 1000
    fn.save(f'tmp2-{weight}.sfd')
    fn.close()

    print('作成')
    name = 'TamaTou'
    copyright = 'Copyright (c) 2022, Hiroshi Miura (https://github.com/hirmiura) with Reserved Font Name TamaTou.'
    version = '1.0.0'
    license = 'Open Font License'
    fn = fontforge.open(f'tmp1-{weight}.sfd')
    fn.fontname = name
    fn.familyname = name
    fn.fullname = name
    fn.weight = weight
    fn.version = version
    fn.sfntRevision = None
    fn.copyright = copyright
    fn.appendSFNTName(0x411, 0, copyright)
    fn.appendSFNTName(0x411, 1, name)
    fn.appendSFNTName(0x411, 2, '')
    fn.appendSFNTName(0x411, 3, '')
    fn.appendSFNTName(0x411, 4, name)
    fn.appendSFNTName(0x411, 5, version)
    fn.appendSFNTName(0x411, 6, name + '-' + weight)
    fn.appendSFNTName(0x411, 7, '')
    fn.appendSFNTName(0x411, 8, '')
    fn.appendSFNTName(0x411, 9, '')
    fn.appendSFNTName(0x411, 10, '')
    fn.appendSFNTName(0x411, 11, '')
    fn.appendSFNTName(0x411, 12, '')
    fn.appendSFNTName(0x411, 13, license)
    fn.appendSFNTName(0x411, 14, '')
    fn.appendSFNTName(0x411, 15, '')
    fn.appendSFNTName(0x411, 16, name)
    fn.appendSFNTName(0x411, 17, '')
    fn.appendSFNTName(0x409, 0, copyright)
    fn.appendSFNTName(0x409, 1, name)
    fn.appendSFNTName(0x409, 2, '')
    fn.appendSFNTName(0x409, 3, '')
    fn.appendSFNTName(0x409, 4, name)
    fn.appendSFNTName(0x409, 5, version)
    fn.appendSFNTName(0x409, 6, name + '-' + weight)
    fn.appendSFNTName(0x409, 7, '')
    fn.appendSFNTName(0x409, 8, '')
    fn.appendSFNTName(0x409, 9, '')
    fn.appendSFNTName(0x409, 10, '')
    fn.appendSFNTName(0x409, 11, '')
    fn.appendSFNTName(0x409, 12, '')
    fn.appendSFNTName(0x409, 13, license)
    fn.appendSFNTName(0x409, 14, '')
    fn.appendSFNTName(0x409, 15, '')
    fn.appendSFNTName(0x409, 16, name)
    fn.appendSFNTName(0x409, 17, '')
    # fn.mergeFonts(f'tmp1-{weight}.sfd')
    fn.mergeFonts(f'tmp2-{weight}.sfd')
    fn.save(f'tmp3-{weight}.sfd')
    fn.generate(f'TamaTou-{weight}.otf')
    fn.close()
