import matplotlib.pyplot as plt

index=['Jazz','Yeast','usair','hamster','foodweb','foodweb2','political-blogs','contact','celegan','worldTrade','Router']    # 以0开始的递增序列作为x轴数据
#开启一个窗口，num设置子图数量，figsize设置窗口大小，dpi设置分辨率
fig = plt.figure(num=1, figsize=(15, 8),dpi=80)
CN = [
    0.958961474 ,   0.87354386   , 0.920920921,
    0.763851533  ,  0.591731266 ,   0.65245478 ,
    0.91741619    ,0.956363636,
    0.928781204   , 0.911522634,    0.547656976

]
Jaccard = [
    0.947236181 ,   0.868491228  ,  0.884884885,
    0.761430877  ,  0.534883721 ,   0.572351421 ,
    0.874897792,
    0.946060606 ,   0.765785609,    0.621399177 ,   0.549847338

]
RA = [0.963149079,	0.876350877,	0.923923924	,0.770216963	,
      0.662790698,	0.645994832,	0.917552467,	0.963636364	,
      0.966226138,	0.901234568,	0.550245586

]
AA = [
    0.978224456 ,   0.875298246  ,  0.935435435  ,
    0.769948001 ,   0.645994832 ,   0.549095607 ,
    0.919324067,
    0.963030303 ,   0.965124816 ,   0.905349794 ,   0.549681402

]
PA = [
    0.804020101  ,  0.824070175 ,   0.867867868 ,   0.863188094 ,
    0.704134367 ,   0.679586563 ,   0.900790406,
    0.973333333 ,   0.87041116 ,   0.905349794 ,   0.496349396

]
Katz = [
    0.989949749,    0.90245614 ,   0.936936937 ,   0.905325444,    0.664082687  ,  0.679586563 ,   0.929681112,
    0.976363636 ,   0.970631424  ,  0.909465021 ,   0.456591

]
CRA = [	0.97319933,	0.803157895,	0.886886887	,0.61161915	,
           0.636950904,	0.647286822,	0.888798038,	0.953939394	,
           0.921071953,	0.930041152,	0.506371963

]

#直接用plt.plot画图，第一个参数是表示横轴的序列，第二个参数是表示纵轴的序列
plt.plot(index,CN,'--o',label='CN')
plt.plot(index,Jaccard,'--o',label = 'Jaccard')
plt.plot(index,RA ,'--o',label = 'RA')
plt.plot(index,AA,'--o',label = 'AA')
plt.plot(index,PA,'--o',label = 'PA')
plt.plot(index,Katz,'--o',label = 'Katz')
plt.plot(index,CRA,'--o',label = 'CRA')
plt.legend()  #显示上面的label
plt.title('AUC')
#显示绘图结果
plt.show()
