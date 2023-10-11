#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
sound/          #最顶层文件
__init__.py     #初始化音频包

formats/        #文件格式转换的子包
__init__.py
wavread.py
wavwrite.py
aiffread.py
aiffwrite.py
auread.py
auwrite.py

effects/        #声音效果的子包
__init__.py
echo.py
surround.py
reverse.py

filters/        #过滤器的子包
__init__.py
equalizer.py
vocoder.py
karaoke.py
"""
########【绝对导入】########
"""当包内含多个子包时，可以用【绝对导入】指定相应的子包或子模块.

例如：模块 sound.filters.vocoder 需要 sound.effects包中的 echo 模块，
可以：from sound.effects import echo
"""

########【相对导入】########
"""也可以用【相对导入】.

相对导入时以当前模块名称为基础的，因为主模块名称总是 __main__，所以python中当作主模块的模块必须使用绝对导入
"""
#例如：从 sound.effects 的 surround 模块导入
'''
from . import echo   #从当前 sound.effects 包下导入 echo 模块
from .. import formats  #从 sound 导入和 effects 同级的 formats 子包
from ..filters import equalizer     #从和 effects 同级的 filters 子包导入 equalizer 模块
'''