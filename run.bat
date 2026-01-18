@echo off
title Tokyo Subway Search System
echo ========================================
echo   东京地铁查询系统启动脚本
echo   Tokyo Subway Search System
echo ========================================
echo.

rem 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.x
    pause
    exit /b 1
)

echo 正在安装依赖包...
pip install -r requirements.txt

if errorlevel 1 (
    echo 错误: 依赖包安装失败
    pause
    exit /b 1
)

echo.
echo 依赖包安装完成！
echo.
echo 启动东京地铁查询系统...
echo 访问地址: http://localhost:5000
echo.
echo 按 Ctrl+C 停止服务器
echo.

python app.py

pause