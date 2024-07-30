from model_utils import ModelTraining

trainer = ModelTraining("breast_cancer_dataset.xlsx")

# model oluşturma
#knn_model = trainer.create_knn_model()
# model kaydetme
#trainer.save_model(knn_model, "trained_models/knn_model")  
# model yükleme
loaded_knn_model = trainer.load_model("trained_models/knn_model") 

#svm_model = trainer.create_svm_model()
#trainer.save_model(svm_model, "trained_models/svm_model")
#loaded_svm_model = trainer.load_model("trained_models/svm_model") 

#decision_tree_model = trainer.create_decision_tree_model()
#trainer.save_model(decision_tree_model, "trained_models/decision_tree_model")
#loaded_decision_tree_model = trainer.load_model("trained_models/decision_tree_model")

trainer.calculate_evaluation_metrics(loaded_knn_model)
trainer.plot_roc_curve(loaded_knn_model)


