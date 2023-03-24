bat_capacity = float(input("Informe a capacidade nominal da bateria em Ah:"))
bat_capacity_now = float(input("a bateria esta a qtos porcentos de sua capacidade nominal?"))
dcdc_efficiency = float(input("Qual a eficiência do conversor DC/DC?"))
tx_periode = float(input("entre com o período (s) do modo TX)"))
tx_duty = float(input("informe o tempo (s)de tx ON:"))
tx_on_current = float(input("informe a corrente de tx on(mA):"))
rx_periode = float(input("informe o periodo (s)do modo rx:"))
rx_duty = float(input("informe o tempo (s)de rx ON:"))
rx_on_current = float(input("informe a corrente de rx on(mA):"))
power_down_on_current = float(input("informe a corrente em sleep mode (uA):"))
sensor_current = float(input("Informe a corrente de consumo(cte) do sensor:"))
tx_rate = tx_duty/tx_periode
tx_current = tx_rate*tx_on_current
rx_rate = ((tx_periode-rx_periode)/rx_periode)*rx_duty/tx_periode
rx_current = rx_rate*rx_on_current
power_down_rate = 1-rx_rate
power_down_current = power_down_rate*power_down_on_current/1000
Iin = (tx_current+rx_current+power_down_current+sensor_current)/dcdc_efficiency
print(Iin)
total_time= bat_capacity*bat_capacity_now/Iin
print("O tempo total de operação do nó sensor é: ", total_time*1000)


