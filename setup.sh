# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:32:19 2021

@author: Sindhu Mallya
"""

mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml