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

![svm_metrics](https://github.com/user-attachments/assets/268f5c46-cb44-449d-9be0-92db217b9d93)     ![svm_conf_matrix](https://github.com/user-attachments/assets/2fa20288-0888-490a-ae96-e070fb0adea9)     ![svm_roc_curve](https://github.com/user-attachments/assets/62cdd0ab-4fb8-4c6b-92e2-18ed8e582e5c)


Decision Tree

![tree_metrics](https://github.com/user-attachments/assets/4875d9cb-a19d-4527-afb7-fad425630f5f)     ![tree_conf_matrix](https://github.com/user-attachments/assets/98c133c5-e7a7-40f7-8548-133031eaf8a8)     ![tree_roc_curve](https://github.com/user-attachments/assets/abe02660-6a19-4189-a336-a4e33e41afea)













