# Meme Kanseri Teşhisi

Bu projede makine öğrenimi modelleri kullanarak meme kanseri teşhisi üzerine çalıştım. 

## Veri Seti
Kullanılan [veri seti](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) Wisconsin Üniversitesi tarafından sağlanmış olup, UCI Machine Learning Repository sitesinden alınmıştır. Veri seti, 30 özellik ve 569 örnekten oluşmaktadır. Özellikler, bir meme kütlesinin ince iğne aspirasyonunun (FNA) sayısallaştırılmış görüntüsünden hesaplanır, görüntüde bulunan hücre çekirdeklerinin özelliklerini açıklarlar. 
M = malignant(kötü huylu), B = benign(iyi huylu) olacak şekilde 2 sınıftan oluşmaktadır. Veri seti, M -> 1, B -> 0 olacak şekilde sayısallaştırılarak güncellenmiştir.

Veri setini eğitmek ve değerlendirmek için üç makine öğrenimi modeli kullandım: KNN, SVM, Decision Tree

KNN: KNN, bir veri noktasını en yakın komşuları arasındaki çoğunluk sınıfına göre sınıflandıran basit bir örnek tabanlı öğrenme algoritmasıdır.
SVM: SVM, özellik uzayında farklı sınıflar arasındaki marjini maksimize eden optimal hiper düzlemi bulan denetimli bir öğrenme modelidir.
Decision Tree: Karar ağacı, kararların ve olası sonuçların ağaç benzeri bir grafiğini kullanan bir modeldir. Özelliklere dayalı tahminler yapmak için veriyi dallara ayırır.

Her model için elde edilen performans metrikleri, karmaşıklık matrisi ve roc eğrisi aşağıda gösterilmiştir:

### KNN

![knn_metrikler5](https://github.com/user-attachments/assets/fbbff935-f3ea-4861-a47d-a4ff913be524)     ![knn_conf_matrix2](https://github.com/user-attachments/assets/debd77dd-df93-4aac-a2df-679f5f31a77e)     ![knn_roc_curve2](https://github.com/user-attachments/assets/53cd0a07-0f60-47d8-b08e-2000561fc4b1)


### SVM

![svm_metrics](https://github.com/user-attachments/assets/268f5c46-cb44-449d-9be0-92db217b9d93)     ![svm_conf_matrix](https://github.com/user-attachments/assets/2fa20288-0888-490a-ae96-e070fb0adea9)     ![svm_roc_curve](https://github.com/user-attachments/assets/62cdd0ab-4fb8-4c6b-92e2-18ed8e582e5c)


### Decision Tree

![tree_metrics](https://github.com/user-attachments/assets/4875d9cb-a19d-4527-afb7-fad425630f5f)     ![tree_conf_matrix](https://github.com/user-attachments/assets/98c133c5-e7a7-40f7-8548-133031eaf8a8)     ![tree_roc_curve](https://github.com/user-attachments/assets/abe02660-6a19-4189-a336-a4e33e41afea)













