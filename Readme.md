 #Readme
 > 要從非頂層執行測試用例的話, 需要調整log的輸出位置, 且subprocess無法生效, 加上pytest.main配上logging模塊不會有問題, 
>所以按原有方案(pytest.main + logging)就行