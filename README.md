# Meme Kanseri Teşhisi

Bu projede makine öğrenimi modelleri kullanılarak meme kanseri teşhisi üzerine çalışılmıştır. 

## Veri Seti
Kullanılan [veri seti](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) Wisconsin Üniversitesi tarafından hazırlanmış olup, UCI Machine Learning Repository sitesinden alınmıştır. Veri seti, 30 özellik ve 569 örnekten oluşmaktadır. Özellikler, bir meme kütlesinin ince iğne aspirasyonunun (FNA) sayısallaştırılmış görüntüsünden hesaplanmıştır ve görüntüde bulunan hücre çekirdeklerinin özelliklerini açıklamaktadırlar. Veri seti, M = malignant (kötü huylu), B = benign (iyi huylu) olacak şekilde 2 sınıftan oluşmaktadır. Bu değerler, M -> 1, B -> 0 olacak şekilde sayısallaştırılarak güncellenmiştir.

Veri setini eğitmek ve değerlendirmek için üç makine öğrenimi modeli kullanılmıştır: KNN, SVM, Decision Tree

KNN (K-Nearest Neighbors): Yeni bir veri noktasını sınıflandırmak için en yakın k komşusunun sınıfına bakarak karar veren denetimli bir öğrenme yöntemidir.

SVM (Support Vector Machine): Veri noktalarını farklı sınıflara ayırmak için en iyi ayırıcı çizgiyi (veya hiper düzlemi) bulan denetimli bir öğrenme yöntemidir. Bu çizgi, sınıflar arasındaki en büyük marjini sağlamaya çalışır.

Decision Tree: Veri noktalarını özelliklerine göre dallara ayırarak karar veren denetimli bir öğrenme yöntemidir. Her düğüm bir özelliği, her dal bir karar kuralını ve her yaprak son kararı temsil eder.

Her modelin eğitilmesi sonucu elde edilen performans metrikleri, karmaşıklık matrisi ve roc eğrisi aşağıda gösterilmiştir:

### KNN

![knn_metrikler5](https://github.com/user-attachments/assets/fbbff935-f3ea-4861-a47d-a4ff913be524)     ![knn_conf_matrix2](https://github.com/user-attachments/assets/debd77dd-df93-4aac-a2df-679f5f31a77e)     ![knn_roc_curve2](https://github.com/user-attachments/assets/53cd0a07-0f60-47d8-b08e-2000561fc4b1)


### SVM

![svm_metrics](https://github.com/user-attachments/assets/268f5c46-cb44-449d-9be0-92db217b9d93)     ![svm_conf_matrix](https://github.com/user-attachments/assets/2fa20288-0888-490a-ae96-e070fb0adea9)     ![svm_roc_curve](https://github.com/user-attachments/assets/62cdd0ab-4fb8-4c6b-92e2-18ed8e582e5c)


### Decision Tree

![tree_metrics](https://github.com/user-attachments/assets/4875d9cb-a19d-4527-afb7-fad425630f5f)     ![tree_conf_matrix](https://github.com/user-attachments/assets/98c133c5-e7a7-40f7-8548-133031eaf8a8)     ![tree_roc_curve](https://github.com/user-attachments/assets/abe02660-6a19-4189-a336-a4e33e41afea)













