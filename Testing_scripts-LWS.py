import time
import requests
import multiprocessing
import concurrent.futures

print(' #########################################################################################################')
print(' $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print(' ################# WELCOME TO LWS BACKEND TEST##########################################################')
print(' ##########TEST STARTS IN 2 SEC ......')
time.sleep(2)
start = time.perf_counter()
######################################### Method Def #################################################################
def login():
    login_time_start =time.perf_counter()
    loginresponse=requests.post('https://api.beldex.dev/login', json={"address":"9yQAHjrzPSeBP2e159vhrcSzB66a4GCvNV8edvVNDAKvG66BLZNoPbi3DRBrfUbjXciFaTSff1bC2MCpqXJm7Dca9NR5JFY","view_key":"2820852e4fc6e5b96f62bb7632541c96b363441e6f2dbb8e50c07671b5b90401","create_account":True,"generated_locally":False})
    login_stop = time.perf_counter()
    print('login response',loginresponse.status_code,'\n',f'login got response in {round(login_stop - login_time_start,3)}sec(s)\n')
    
def get_address_info():
    address_info_start =time.perf_counter()
    address_info_response = requests.post('https://api.beldex.dev/get_address_info', json={"address":"9yQAHjrzPSeBP2e159vhrcSzB66a4GCvNV8edvVNDAKvG66BLZNoPbi3DRBrfUbjXciFaTSff1bC2MCpqXJm7Dca9NR5JFY","view_key":"2820852e4fc6e5b96f62bb7632541c96b363441e6f2dbb8e50c07671b5b90401"})
    address_info_stop =time.perf_counter()
    print('get_address info',address_info_response.status_code,'\n',f'address_info got response in {round(address_info_stop - address_info_start,3)}sec(s)\n')

def get_address_txs():
    address_txs_start = time.perf_counter()
    address_txs_response =requests.post('https://api.beldex.dev/get_address_txs', json={"address":"9yQAHjrzPSeBP2e159vhrcSzB66a4GCvNV8edvVNDAKvG66BLZNoPbi3DRBrfUbjXciFaTSff1bC2MCpqXJm7Dca9NR5JFY","view_key":"2820852e4fc6e5b96f62bb7632541c96b363441e6f2dbb8e50c07671b5b90401"})
    address_txs_stop =time.perf_counter()
    print('get_address_txs response ',address_txs_response.status_code,'\n',f'address_txs in {round(address_txs_stop - address_txs_start,3)}sec(s)\n')


def get_unspent_outs():
    unspent_outs_start = time.perf_counter()
    unspent_outs_response = requests.post('https://api.beldex.dev/get_unspent_outs', json={"address":"9yQAHjrzPSeBP2e159vhrcSzB66a4GCvNV8edvVNDAKvG66BLZNoPbi3DRBrfUbjXciFaTSff1bC2MCpqXJm7Dca9NR5JFY","view_key":"2820852e4fc6e5b96f62bb7632541c96b363441e6f2dbb8e50c07671b5b90401","amount":"0","dust_threshold":"2000000000","use_dust":True,"mixin":9})
    unspent_outs_stop =time.perf_counter()
    print ('unspent outs response ',unspent_outs_response.status_code,'\n',f'unspent_outs got reponse in {round(unspent_outs_stop - unspent_outs_start,3)}sec(s)\n')

def get_random_outs():
    random_outs_start = time.perf_counter()
    random_outs_respose =requests.post('https://api.beldex.dev/get_random_outs', json={"amounts":["0","0","0","0"],"count":10})
    random_outs_stop = time.perf_counter()
    print ('random puts reponse',random_outs_respose.status_code,'\n',f'random_outs got reponse in {round(random_outs_stop - random_outs_start,3)}sec(s)\n')

def submit_raw():
    submit_raw_start = time.perf_counter()
    submit_raw_response = requests.post('https://api.beldex.dev/submit_raw_tx', json={"address":"9yQAHjrzPSeBP2e159vhrcSzB66a4GCvNV8edvVNDAKvG66BLZNoPbi3DRBrfUbjXciFaTSff1bC2MCpqXJm7Dca9NR5JFY","view_key":"2820852e4fc6e5b96f62bb7632541c96b363441e6f2dbb8e50c07671b5b90401","tx":"04020000000202000a9eed11b4f40193d003a5d303fe62f707f939c523d802fa0ca38336e41a28840e8cce4d4e72455de68280a0f52aedd29c070220581becb10502000abbc316bbb404c567d6436ecb2beb03a301ce04e80337686a6aae968b3dcf61609ca33f961df72933680e3600d06a10b1375bb9558602000219ab09f6c5a0a46864c04b9f45821c803cf7113eadbcff7a3a0dfa0fd0909f5700028062c7da21633b413b28462a1025dc58e80705b2d6fccc7125d89e8aa23524c92c01ba4f1e93835167c18f79e81f4a9ca33364aefa11e7358d65f3fbc13143e24b0f020901f9548c5bd9f06bad00058ec583014e8067d1c6d3e414e16f357bcdfd5fc649266935ca6fe11633357082e9995710170c589e3d12bffbdde001e13be490a8e159000e2853dbce77b9136ba12043df01ac3de6ad93f59d192feff4d62bd81f015c6ac4a928792cb926588015e30b39359b7da2eaa8c4757ea44404ffb3e3e8d5445ee63a857a0baad2db5519e9661b0f0b292efa5641db47133678cd57a81e9a4934a18a0946a8e70d9629e23541a77d7f48dfa3860415271e99d207d4959d3d5fd0d2ae22d0d04f8c5f51b911536c186a61e10b4466ae7db177f94014fd229e3e50c40c567a9630b906908ac9d8a430ac2b160b7d047c784d738b3bdc321a0ac387f67faf970498a6c460e2f0fc5545715dfabbdcd5a7eff2f6e27774ada80907c83ae185b253b2bbad4d9064bd02c711e18ec6287448c6eb8ddb6640a811802e547c8e2c330c73a3700f96308a13121a111eca2f0d440a796c09c4bb4307d025d58f871cfe207845b57eea91e6a716c73f6b6839f9af46d8d59323043a0b0243b820ae796480fc4740496a9e432e64f313b8614aecc1a4619e41fd07f60d6feea0a1d58de9e13fc04edd6306aa9cb52a8cebe4d23f8ba1d183a318524dc1e537c228c24d9f095b63ee1935851420b23033fbbf23a28b2710cdad1c90408a43ccf72a77234985fa9e2a5938e509e9ea6138708a684848a7de06c1f16d55a4398307129fe2d582c3930bef5417b6b8b9526f4f2cb0168fa25346946de333764dfd3d3fde20b7c59357af6232045d49d672ed1aabac8d118d146227b5501c2adb85fb17a9e6f5971098bd4c672818c2659482d40fae506ea78062e03ba9ea91f948cdfe718a0c122e7f577060a6a8442bfe3feb42df144856101f8d0624c3e6b55c45d1401f2cf5d412ee9065c1e65301639378e6fb49b0867308eba3830ac7af18e12e689cbe78e61777e8dd86188ac87d53f57a0fdfbf4131d746fdcfe896f4781b14bcb261792901639abb7b0b89bc2e3252ef2a821f0507acd7d4a481b15c2a8e1b347090c1c6a8520324c6229ba0354d25e92aa61cd45d176b4670925485a000af4e20df112ba42680884820ad0d119f8d271fccbdf4eab7965d6e3df433070c83cc2ba6afbe1a2eced3fd65101725b7ad6981680f62f0dcf78966aad014a8069ea2f0df6641cce12e271eb9d9d300794fdf9c6f5dff3f89761bf5832c40ab0f54de402ec41dfc2647feda00e136ef4514d7ebac1f8c42e94ce96bf1b7a97a020dd33895e10b5911484d37d96274f09fe7f50a3da56c1958be41b48e21a7e60d5ee7470046b4e725e9b17fd2d026065824359e02e27049d6b73ea49a69ed4305a3ddb36cdbee0ad18eb3b29292d65378c4f59f43effe2a21b41966e9f1a4ba0327302cd9deadc341a407e1099e247410574d762abfd8210b6b39eabca1a3dd0c0bf8d8a218715d5f036a4bcea21ee99813d499f496ea8f74e46448e961c43509806cae3d59dbf7c8e7699654a40f80a37c5fa8e8411c17ff82403af15566230d235581494f7d22dd85f9e79c393def27cd21a4bb9e134ca80b93f50081f84709ff9f0a14eb1c8c661431d768a8141f76cd94c91b5ac48c59b99c2c658f453e037906a0f8730970a063f60bd4f958e3adc1ac9feff5777ba7da460170829a500d99df0bb06c5bf4c0f2d0e950829682869373f3d65342e7ce7e1de9e8d1b8015ecaaa8d5ea188537e52a1963ed2b07aec33048bb9c8dc91410ea42daf17ffe2098beba5a482de55b51bf5fb9967c986dc70ddcba8dd54955070f5a7e1e0124c0e7d11312fe6615359fd4ece04b70cd5c87406ff40ebe5cb2d8c6519481f73db055c94de76b484f2e95e193a2ce240b7292e28e89ee37190638ac3c9d4f0cd4d0958f01ddf31dec059710f672864506445ec61a0e296d9ce179542b482203b380afc0f7027d657a96e8b703cbce0856090e5bfe76638ff40967af31f0712dcfe023737c8c28468192802f007a98741680d7208a1e1cca43f441864996a9b59b500ff64fea80094322003cb2502eb10214ee3976b2ec4a924b0f341e99545cf150895601a015328e4d908e166106eaa84b1055f86164a0abb405fd24542bd72830e0bb66a733ce956dd0f042216ddc713d209c9a9b50363e8f6639141aa1825330e581a88d9567b354232954d7cc8466a2efea65bd8647b9c7ed98bcbb4f439270e8cc23c4974bf964257fbab375a6dd6af4c74e704b218a1bbe928c926ff26f6b4453d78d12250910b77dfa2f5c21c9836bab1650f909efbeb9ccd8c5fed4306f1c977f1b84d65e53b184aa088967791e817133d81424317a47be355c5e48edd44"})
    submit_raw_stop = time.perf_counter()
    print ('submit raw response',submit_raw_response.status_code,'\n',f'submit_raw_txs got reponse in {round(submit_raw_stop - submit_raw_start,3)}sec(s)','\n\n')
###################################################################################################################################################################################

############################### Method running in seq #########################
login()
get_address_info()
get_address_txs()
get_unspent_outs()
get_random_outs()
submit_raw()
################################# Endpoints in parallel ###############################################################
Multistart = time.perf_counter()
p1 = multiprocessing.Process(target=login)
p2 = multiprocessing.Process(target=get_address_info)
p3 = multiprocessing.Process(target=get_address_txs)
p4 = multiprocessing.Process(target=get_unspent_outs)
p5 = multiprocessing.Process(target=get_random_outs)
p6 = multiprocessing.Process(target=submit_raw)

p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()

p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join() #join will make sure the process is completed . this will help us to calculate the time for test
Multistop = time.perf_counter()
print(f'\nTime for parallel process for all the multiprocessing{round(Multistop - Multistart,4)}sec(s)\n')

###########################################################################################################################
finish = time.perf_counter()
print(f'\nTotal test Finished in {round(finish-start,3)}second(s)')

###########################################################################################################################

# Endpoint Parallel test according to user requirement 
def login_multiprocessing():
    ######## Login Start ####################
    val1 = input("\n please Enter no of parallel process for [login method ] you want to run : ")
    val1 =int(val1)

    login_st = time.perf_counter()
    login_process =[]

    for _ in range(val1):
        p_login = multiprocessing.Process(target=login)
        p_login.start()
        login_process.append(p_login)

    for process in login_process:
        process.join()

    login_stp = time.perf_counter()
    print(f'\nlogin parallel test Finished in {round(login_stp - login_st,4)}sec(s)')
    ############ Login End $$$$$$$$$$$$$$$$$$

def get_address_info_multiprocessing():
    ###### Get Address_info Start ################
    val2 = input("\nplease Enter no of parallel process for [Get_address_info method ] you want to run : ")
    val2 =int(val2)

    add_info_st = time.perf_counter()
    add_info_process =[]

    for _ in range(val2):
        p_info = multiprocessing.Process(target=get_address_info)
        p_info.start()
        add_info_process.append(p_info)

    for process in add_info_process:
        process.join()

    add_info_stp = time.perf_counter()
    print(f'\n get_address_info parallel test Finished in {round(add_info_stp - add_info_st,4)}sec(s)')

    ############ Get_Address_info Stop $$$$$$$$$$$$$$$$$

def get_address_txs_multiprocessing():
    ############ Get Address_txs Start $$$$$$$$$$$$$$$$$
    val3 = input("\nplease Enter no of parallel process for [Get_address_txs method ] you want to run : ")
    val3 =int(val3)
    add_tx_st = time.perf_counter()
    add_tx_process =[]

    for _ in range(val3):
        p_tx = multiprocessing.Process(target=get_address_txs)
        p_tx.start()
        add_tx_process.append(p_tx)

    for process in add_tx_process:
        process.join()

    add_tx_stp = time.perf_counter()
    print(f'\n get_address_txs parallel test Finished in {round(add_tx_stp - add_tx_st,4)}sec(s)')

    ################    Get Address_txs stop    $$$$$$$$$$$$$$$$$$$$$$$$$

def get_unspent_outs_multiprocessing():
    ################    Get Unspent outs start $$$$$$$$$$$$$$$$$$$$
    val4 = input("\nplease Enter no of parallel process for [get_unspent_outs method ] you want to run : ")
    val4 =int(val4)

    add_un_st = time.perf_counter()
    add_un_process =[]

    for _ in range(val4):
        p_un = multiprocessing.Process(target=get_unspent_outs)
        p_un.start()
        add_un_process.append(p_un)

    for process in add_un_process:
        process.join()

    add_un_stp = time.perf_counter()
    print(f'\n get_unspent_outs parallel test Finished in {round(add_un_stp - add_un_st,4)}sec(s)')
    ################    Get Unspent outs stop ##########################

def get_random_outs_multiprocessing():
    ################    Get Random outs start $$$$$$$$$$$$$$$$$$$$
    val5 = input("\nplease Enter no of parallel process for [get_random_outs method ] you want to run : ")
    val5 =int(val5)

    add_ran_st = time.perf_counter()
    add_ran_process =[]

    for _ in range(val5):
        p_ran = multiprocessing.Process(target=get_random_outs)
        p_ran.start()
        add_ran_process.append(p_ran)

    for process in add_ran_process:
        process.join()

    add_ran_stp = time.perf_counter()
    print(f'\n get_random_outs parallel test Finished in {round(add_ran_stp - add_ran_st,4)}sec(s)')
    ################    Get Random outs stop ##########################

def submit_raw_multiprocessing():
    ################    Get Submit_raw start $$$$$$$$$$$$$$$$$$$$
    val6 = input("\nplease Enter no of parallel process for [submit_raw method ] you want to run : ")
    val6 =int(val6)

    add_subtx_st = time.perf_counter()
    add_subtx_process =[]

    for _ in range(val6):
        p_subtx = multiprocessing.Process(target=submit_raw)
        p_subtx.start()
        add_subtx_process.append(p_subtx)

    for process in add_subtx_process:
        process.join()

    add_subtx_stp = time.perf_counter()
    print(f'\n submit_raw parallel test Finished in {round(add_subtx_stp - add_subtx_st,4)}sec(s)')
    ################    Get Submit_raw stop ##########################

def final_stress_test():
    val7 = input('\n Please Enter No of Parallel Process for All the Endpoints you want to run : ')
    val7 = int(val7)
    fin_st = time.perf_counter()

    final_log = []
    final_add_info = []
    final_add_txs = []
    final_unspent = []
    final_random =[]
    final_tx_send= []

    for _ in range(val7):
        p_log_st = multiprocessing.Process(target=login)
        p_log_st.start()
        p_info = multiprocessing.Process(target=get_address_info)
        p_info.start()
        p_tx = multiprocessing.Process(target=get_address_txs)
        p_tx.start()
        p_un = multiprocessing.Process(target=get_unspent_outs)
        p_un.start()
        p_ran = multiprocessing.Process(target=get_random_outs)
        p_ran.start()
        p_subtx = multiprocessing.Process(target=submit_raw)
        p_subtx.start()

        final_log.append(p_log_st)
        final_add_info.append(p_info)
        final_add_txs.append(p_tx)
        final_unspent.append(p_un)
        final_random.append(p_ran)
        final_tx_send.append(p_subtx)

        for process in final_log:
            process.join()
        for process in final_add_info:
            process.join()
        for process in final_add_txs:
            process.join()
        for process in final_unspent:
            process.join()
        for process in final_random:
            process.join()
        for process in final_tx_send:
            process.join()
    
    fin_stp = time.perf_counter()
    print(f'\n final test parallel test Finished in {round(fin_stp - fin_st,4)}sec(s)')


        

################################################################################################3333333333###############333333333333333333#####################

while True:
    method = input("\n Which Method do You Want to Do Parallel Test \n Give 1 for Login \n Give 2 for get_address_info \n Give 3 for get_address_txs \n Give 4 for get_unspent_outs \n Give 5 for get_random_outs \n Give 6 for submit_raw \n Give 7 final_stress_test This will hit all the endpoints simantinously \nEnter anything to exit \nPlease Enter you choice here : ")
    method = int(method)
    if method == 1:
        login_multiprocessing()
    elif method == 2:
        get_address_info_multiprocessing()
    elif method == 3:
        get_address_txs_multiprocessing()
    elif method == 4:
        get_unspent_outs_multiprocessing()
    elif method == 5:
        get_random_outs_multiprocessing()
    elif method == 6:
        submit_raw_multiprocessing()
    elif method == 7:
        final_stress_test()
    else:
        print('\n Thanks for Testing :-)')
        break
    
