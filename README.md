Meme Kanseri Teşhisi
Bu projede meme kanseri teşhisi üzerine çalıştım. Veri seti Wisconsin Üniversitesi tarafından hazırlanmış olup UCI Machine Learning Repository sitesinden alındı. 30 özellik, 569 örnekten
oluşmakta. Özellikler, bir meme kütlesinin ince iğne aspirasyonunun (FNA) sayısallaştırılmış görüntüsünden hesaplanır. Görüntüde bulunan hücre çekirdeklerinin özelliklerini açıklarlar.
Diagnosis (M = malignant, B = benign) şeklinde 2 sınıftan oluşmaktadır. M -> kötü huylu, B -> iyi huylu. Veri setinde M değeri 1, B değeri 0 olacak şekilde sayısallaştırılmıştır.

Bu veri seti KNN, SVM, Decision Tree modelleri ile eğitilmiştir. 
KNN hakkında biraz bilgi
SVM hakkında biraz bilgi
Decision Tree hakkında biraz bilgi

Ve eğitim sonucunda her model için elde edilen doğruluk parametreleri:

![knn_metrikler2](https://github.com/user-attachments/assets/5679d052-9aa6-475e-90d3-3af2ff42e86a)     ![knn_conf_matrix1](https://github.com/user-attachments/assets/d57d3eb5-303b-4f58-9c4a-d91b4c360840)     ![knn_roc_curve1](https://github.com/user-attachments/assets/29baccbd-16aa-4e9a-86ea-12ea8e75befb)



