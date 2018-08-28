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
    
# 消息机制
- 消息的传递机制
    - 自动发出事件/消息
    - 消息有系统负责发送到队列
    - 由相关组件进行绑定/设置
    - 后端自动选择感兴趣的事件并做出相应反应
    
- 消息格式：
    - <[modifier-]---type-[-detail]>
    - e.g <Button-1>: Button表示一个按钮事件，1代表的是鼠标左键，2代表中键
    - e.g <KeyPress-A>: 按下A键
    - e.g <Control-Shift-KeyPress-A>: 同时按下control, shift, A 三个按键
    - [键位对应名称]
    (https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html)
    
# 绑定
- bind_all: 全局范围的绑定，默认的是全局快捷键，例如F1是帮助文档
- bind_class: 接受三个参数，第一个是类名，第二个是事件，第三个是操作
    - w.bind_class("Entry", "Control-V", my_paste)
- bind: 单独对某一个实例绑定
- unbind： 解绑，需要一个参数，即你要解绑哪个事件

## Entry
- 输入框，功能单一
- entry["show"] = "*", 设置遮挡字符，输入密码时使用


# 菜单
1. 普通菜单
    - 第一个Menu类定义的是parent
    - add_command 添加菜单项，如果菜单是顶层菜单，则从左向右添加，否则就是下拉菜单
    - label： 指定菜单项名称
    - command: 点击后相应的调用函数
    - acceletor： 快捷键
    - underline： 制定是否菜单信息下有横线
    - menu：属性制定使用哪一个作为顶级菜单
    
2. 级联菜单
    - add_cascade:级联菜单，作用是引出后面的菜单
    - add_cascade的menu属性：指明把菜单级联到哪个菜单上
    - label： 名称
    - 过程：
        - 建立menu实例
        - add_command
        - add_cascade
        
# canvas
- 画布： 可以自由的在上面绘制图形的一个小舞台
- 在画布上绘制对象， 通常用create_xxxx，xxxx=对象类型， 例如line，rectangle
- 画布的作用是把一定组件画到画布上显示出来
- 画布所支持的组件：
    - arc
    - bitmap
    - image(BitmapImage, PhotoImage)
    - line
    - oval
    - polygon
    - rectangle
    - text
    - window（组件）
- 每次调用create_xxx都会返回一个创建的组件的ID，同时也可以用tag属性指定其标签
- 通过调用canvas.move实现一次性动作