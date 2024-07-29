Meme Kanseri Teşhisi
Bu projede meme kanseri teşhisi üzerine çalıştım. Veri seti Wisconsin Üniversitesi tarafından hazırlanmış olup UCI Machine Learning Repository sitesinden alındı. 30 özellik, 569 örnekten
oluşmakta. Özellikler, bir meme kütlesinin ince iğne aspirasyonunun (FNA) sayısallaştırılmış görüntüsünden hesaplanır. Görüntüde bulunan hücre çekirdeklerinin özelliklerini açıklarlar.
Diagnosis (M = malignant, B = benign) şeklinde 2 sınıftan oluşmaktadır. M -> kötü huylu, B -> iyi huylu. Veri setinde M değeri 1, B değeri 0 olacak şekilde sayısallaştırılmıştır.

Bu veri seti KNN, SVM, Decision Tree modelleri ile eğitilmiştir. 
KNN hakkında biraz bilgi
SVM hakkında biraz bilgi
Decision Tree hakkında biraz bilgi

Ve eğitim sonucunda her model için elde edilen doğruluk parametreleri:
KNN

![knn_metrikler4](https://github.com/user-attachments/assets/7276f448-efbe-4d63-96a4-5bae10fe7cd7)     ![knn_conf_matrix1](https://github.com/user-attachments/assets/d57d3eb5-303b-4f58-9c4a-d91b4c360840)     ![knn_roc_curve1](https://github.com/user-attachments/assets/29baccbd-16aa-4e9a-86ea-12ea8e75befb)

SVM

![svm_metrikler2](https://github.com/user-attachments/assets/6a996e40-03ea-4b67-86d6-e7e9ba5dbd0a)     ![svm_conf_matrix1](https://github.com/user-attachments/assets/83c76657-177a-4c98-8244-078488f0508b)     ![svm_roc_curve1](https://github.com/user-attachments/assets/d627776d-d48c-499d-b01c-bada7bf454a7)

Decision Tree

![tree_metrikler2](https://github.com/user-attachments/assets/592a81d9-a4be-4eba-83f4-53b0506342f5)     ![tree_conf_matrix1](https://github.com/user-attachments/assets/50b81e56-af26-48a3-be44-6ecb5fef1988)     ![tree_roc_curve1](https://github.com/user-attachments/assets/dc668043-1f7d-4c64-bf95-d18b762c9fea)










