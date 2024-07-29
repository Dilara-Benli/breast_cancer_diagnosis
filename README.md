Meme Kanseri Teşhisi
Bu projede meme kanseri teşhisi üzerine çalıştım. Veri seti Wisconsin Üniversitesi tarafından hazırlanmış olup UCI Machine Learning Repository sitesinden alındı. 30 özellik, 569 örnekten
oluşmakta. Özellikler, bir meme kütlesinin ince iğne aspirasyonunun (FNA) sayısallaştırılmış görüntüsünden hesaplanır. Görüntüde bulunan hücre çekirdeklerinin özelliklerini açıklarlar.
Diagnosis (M = malignant, B = benign) şeklinde 2 sınıftan oluşmaktadır. M -> kötü huylu, B -> iyi huylu. Veri setinde M değeri 1, B değeri 0 olacak şekilde sayısallaştırılmıştır.

Bu veri seti KNN, SVM, Decision Tree modelleri ile eğitilmiştir. 
KNN hakkında biraz bilgi
SVM hakkında biraz bilgi
Decision Tree hakkında biraz bilgi

Ve eğitim sonucunda her model için elde edilen doğruluk parametreleri:

![knn_metrikler](https://github.com/user-attachments/assets/00518c66-9205-4513-9b72-7df275f76380)   ![knn_conf_matrix](https://github.com/user-attachments/assets/d494563b-767c-4859-aac6-74e4d15603ed)   ![knn_roc_curve](https://github.com/user-attachments/assets/85b50327-9a85-40a5-b722-d850c88a3c26)


