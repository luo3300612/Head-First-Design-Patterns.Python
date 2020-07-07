# Head First Design Patterns Python
## Chapter1 Strategy Pattern
策略模式定义了算法族,分别封装起来,让它们之间可以互相替换.此模式让算法的变化
独立于使用算法的客户

设计原则
* 多用组合少用继承

### target
class:
* MallardDuck
* RedheadDuck
* RubberDuck
* DecoyDuck

behaviour:
* fly
* quack

每种行为(fly)包括了一些具体行为(可以飞,不可以飞),将每种行为定义为算法族

## Chapter2 Observer Pattern
### target
气象站,探测温度,湿度,气压,一旦三者发生变化,则传达给三个布告版,
布告版可以动态增加和删除
