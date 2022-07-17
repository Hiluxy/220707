    num_list=['0','1','2','3','4','5','6','7','8','9']
    able_list=[i for i in num_list if i not in no_list]

    combi=[]
    for i in range(1,len(able_list)):
      combi+=list(product(able_list,repeat=i))