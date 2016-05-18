import sys;
import os;

try:
    data_path = sys.argv[1];
    exec_path = sys.argv[2];
    test_exec_path = sys.argv[3];
    test_data_path = sys.argv[4];
except IndexError:
    print('script.py [data] [train_exec] [test_exec] [test_data]');
    exit();

train_dir = exec_path[ : exec_path.rfind('/') ];
data_fname = data_path[ data_path.rfind('/')+1: ];

for l2 in [0.1,0.01]:
    for l1 in [1,0.1,0.01]:
        log_path = train_dir+'/log.'+data_fname+'-l1-'+str(l1)+'-l2-'+str(l2);
        model_path = train_dir+'/model';
        os.system(exec_path+' '+data_path+' '+str(l1)+' '+str(l2)+' 1.0 '+model_path+' > '+log_path+' 2> '+log_path);
        os.system(test_exec_path+' '+test_data_path+' '+model_path +' >> '+log_path+' 2>> '+log_path);
