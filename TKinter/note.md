# Tkinter常用组件
- 按钮
    
        Button                 按钮组件
        RadioButton            单选框组件
        CheckButton            选择按钮组件
        Listbox                列表框组件
        
- 文本输入
        
        Entry           单文本框组件
        Text            多行文本框组件
        
- 标签组件

        label
        Message
        

# 组件的大致使用步骤
1. 创建总面板
2. 创建面板上的各种组件
    1. 指定组件的父组件，即依附关系
    2. 利用相应的属性对组件进行设置
    3. 给组件安排布局
3. 同步骤2相似，创建好多个组件
4. 最后，启动总面板的消息循环

# Button的属性：

        anchor 				设置按钮中文字的对其方式，相对于按钮的中心位置
        background(bg) 		设置按钮的背景颜色
        foreground(fg)		设置按钮的前景色（文字的颜色）
        borderwidth(bd)		设置按钮边框宽度
        cursor				设置鼠标在按钮上的样式
        command				设定按钮点击时触发的函数
        bitmap				设置按钮上显示的图片
        font				设置按钮上文本的字体
        width				设置按钮的宽度  (字符个数)
        height				设置按钮的高度  (字符个数)
        state				设置按钮的状态
        text				设置按钮上的文字
        image				设置按钮上的图片

# 组件布局 - 控制组件的摆放方式
- 三种布局：
    - pack: 按照方位布局
    - place: 按照坐标布局
    - grid： 网格布局
    
- pack布局
    - 最简单，代码量最少，挨个摆放，默认从上倒下，系统自动设置
    - 通用使用方式为: 组件对象.pack(一系列设置）
    - side: 停放位置 -> 可选值为LEFT, TOP, RIGHT, BOTTOM
    - fill: 填充方式 -> X, Y, BOTH, NONE
    - expand: YES/NO
    - anchor: N, E, S, W, CENTER
    - ipadx: x方向的内边距
    - ipady: y方向的内边距
    - padx: x方向外边界
    - pady：y方向外边界
    
- grid布局
    - 通用使用方式：组件对象.grid(一系列设置)
    - 利用row, column编号，都是从0开始
    - sticky：N, E, S, W, 表示上下左右, 用来决定组件从哪个方向开始
    - 支持ipadx，padx等参数，跟pack函数含义一样
    - 支持rowspan，columnspan，表示跨行，跨列数量
    
- place布局
    - 明确方位的摆放
    - 相对位置布局，随意改变窗口大小会导致混乱
    - 使用place函数，分为绝对布局和相对布局，绝对布局使用x，y参数
    - 相对布局使用relx, rely, relheight, relwidth