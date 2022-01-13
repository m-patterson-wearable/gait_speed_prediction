from sklearn.preprocessing import StandardScaler, MinMaxScaler 
import time

# NOTES about feeding data for grid search:
# 1) When defineing data below, we need to provie dat in pairs as follows: 
# The data type: (i.e. 'xyz_raw','xyz_interp','rms_raw','rms_interp','rms_interp')
# The correponding scale applied to features (X)
# The correponding scale applied to target (y). If no scale is desired for target, please enter 'none'
# 2) The same applies whe we provdie data for hidden layers 




model=['cnn']
data=[
    ['xyz_interp','xyz_interp'],
    [StandardScaler(),StandardScaler(),MinMaxScaler()],
    [StandardScaler(),'none', MinMaxScaler()] 
    ]
batch_size=[16,40,80]
epochs=[20,40,80]
conv_layers=[
   ???
]
layers=[
    [[300,400,128, 64],['relu','relu','relu','relu'],[0,0,0,0]],
    [[256,128,128, 64],['relu','relu','relu','relu'],[0.2,0.1,0.1,0]],
    ]
loss=['mean_squared_error']
metrics=[['mean_squared_error']]



def make_run_dic(i_model,i_data,i_batch,i_epochs,i_layers,i_loss,i_metrics):
    run={}
    run['id']=time.time()
    run['model']=model[i_model]
    run['dataset']=data[0][i_data]
    run['scaler_X']=data[1][i_data]
    run['scaler_y']=data[2][i_data]
    run['batch_size']=batch_size[i_batch]
    run['epochs']=epochs[i_epochs]
    run['nodes']=layers[i_layers][0]
    run['act']=layers[i_layers][1]
    run['dropout']=layers[i_layers][2]
    run['loss']=loss[i_loss]
    run['metrics']=metrics[i_metrics]
    return run





grid=[]
for i_model in range(len(model)):
    for i_data in range(len(data[0])):
        for i_batch in range(len(batch_size)):
            for i_epochs in range(len(epochs)):
                for i_layers in range(len(layers)):
                    for i_loss in range(len(loss)):
                        for i_metrics in range(len(metrics)):
                            run=make_run_dic(i_model,i_data,i_batch,i_epochs,i_layers,i_loss,i_metrics)
                            grid.append(run)


print('No. of combinations: {}'.format(len(grid)))












