# # a) Model a curve from the recent previous losses
# def get_fscore(model, max_iterations, n_samples=4):
#     # _losses= [3,5, 2,1,1] 
#     _losses = model.final_loss_history
#     num_samples = n_samples # take the 4 most recent samples to model it
#     losses = np.array(_losses)
#     samples = losses[-num_samples: ]

#     # Get into format [ [x,y], [x,y] ]
#     x = np.arange(len(losses))[-num_samples: ]
#     points = np.column_stack( (x,samples) )
#     a,b = fit_exp(points)
#     #-------------------- Method1: When it has converged
#     # # If it is ascending, that is not ideal
#     # epsilon = -0.1
#     # estimate = epsilon/b
#     # gradient_descending = a*b < 0  # abe^{bx} < 0 <-> ab<0
#     # # It has a trend of getting worse from adding extra nodes to it
#     # h =  0.0 if not gradient_descending else epsilon/b
#     # f_score = h 
#     #------------------- Method2: predict its score after the max no.iterations (simpler)
#     # current_x = x[x.shape[0]-1]; future_x = current_x + 5 # Alternatively maybe just use what its value will be after some turns
#     f_score = a*np.exp(b*max_iterations)
#     return float(f_score)