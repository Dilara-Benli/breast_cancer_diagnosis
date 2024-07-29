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

![knn_metrikler5](https://github.com/user-attachments/assets/fbbff935-f3ea-4861-a47d-a4ff913be524)     ![knn_conf_matrix2](https://github.com/user-attachments/assets/debd77dd-df93-4aac-a2df-679f5f31a77e)     ![knn_roc_curve2](https://github.com/user-attachments/assets/53cd0a07-0f60-47d8-b08e-2000561fc4b1)


SVM

![svm_metrikler2](https://github.com/user-attachments/assets/6a996e40-03ea-4b67-86d6-e7e9ba5dbd0a)     ![svm_conf_matrix1](https://github.com/user-attachments/assets/83c76657-177a-4c98-8244-078488f0508b)     ![svm_roc_curve1](https://github.com/user-attachments/assets/d627776d-d48c-499d-b01c-bada7bf454a7)

Decision Tree

![tree_metrikler2](https://github.com/user-attachments/assets/592a81d9-a4be-4eba-83f4-53b0506342f5)     ![tree_conf_matrix1](https://github.com/user-attachments/assets/50b81e56-af26-48a3-be44-6ecb5fef1988)     ![tree_roc_curve1](https://github.com/user-attachments/assets/dc668043-1f7d-4c64-bf95-d18b762c9fea)










