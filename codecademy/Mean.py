import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18, 9, 2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)

print(store_one_avg)
print(store_two_avg)
print(store_three_avg)

best_seller = store_two

percentage = np.mean(store_one > 4)
print(percentage)

allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])
print(np.mean([6, 2, 5]))
total_mean = np.mean(allergy_trials)
print(total_mean)
trial_mean = np.mean(allergy_trials, axis=1)
print(trial_mean)
patient_mean = np.mean(allergy_trials, axis=0)
print(patient_mean)
