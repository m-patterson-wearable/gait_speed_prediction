from sklearn.preprocessing import StandardScaler, MinMaxScaler 
import time


model=['mlp']
data=[
    ['xyz_raw','xyz_interp','rms_raw','rms_interp','rms_interp'],
    [StandardScaler(),StandardScaler(),StandardScaler(),StandardScaler(),MinMaxScaler()]
    ]
batch_size=[16,80]
epochs=[80,120]
layers=[
    [[128],['relu'],[0]],
    [[256,128],['relu','relu'],[0,0]],
    [[256,128, 64],['relu','relu','relu'],[0,0,0]],
    [[256,128, 64],['relu','relu','relu'],[0.1,0.2,0.1] ]
    ]
loss=['mean_squared_error']
metrics=[['mean_squared_error']]






def make_run_dic(i_model,i_data,i_batch,i_epochs,i_layers,i_loss,i_metrics):
    run={}
    run['id']=time.time()
    run['model']=model[i_model]
    run['dataset']=data[0][i_data]
    run['scaler']=data[1][i_data]
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
    for i_data in range(len(data)):
        for i_batch in range(len(batch_size)):
            for i_epochs in range(len(epochs)):
                for i_layers in range(len(layers)):
                    for i_loss in range(len(loss)):
                        for i_metrics in range(len(metrics)):
                            run=make_run_dic(i_model,i_data,i_batch,i_epochs,i_layers,i_loss,i_metrics)
                            grid.append(run)


print('No. of combinations: {}'.format(len(grid)))














# run1 = {
#     'id': time.time(),
#     'model': 'mlp',
#     'dataset': 'xyz_raw', # options: xyz_raw, rms_raw, xyz_interp,rms_interp
#     'scaler': StandardScaler(),  # standard, minmax, maxabs 
#     'batch_size': 16,
#     'epochs':3,
#     'nodes': [128],  
#     'act': ['relu'],
#     'dropout': [0],  # dropout 0 means keep all nodes
#     'loss': 'mean_squared_error',
#     'metrics': ['mean_squared_error']
# }

# run2 = {
#     'id': time.time(),
#     'model': 'mlp',
#     'dataset': 'rms_raw', # options: xyz_raw, rms_raw, xyz_interp,rms_interp
#     'scaler': StandardScaler(),  # standard, minmax, maxabs 
#     'batch_size': 16,
#     'epochs':3,
#     'nodes': [128],  
#     'act': ['relu'],
#     'dropout': [0],  # dropout 0 means keep all nodes
#     'loss': 'mean_squared_error',
#     'metrics': ['mean_squared_error']
# }


# grid=[run1, run2]
