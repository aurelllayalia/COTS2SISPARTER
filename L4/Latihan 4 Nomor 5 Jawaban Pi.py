#Import mpi4py
from mpi4py import MPI

#Membuat fungsi dekomposisi bernama local_loop 
#Local_loop akan menghitung setiap bagiannya
#Menggunakan 4/(1+x^2), perhatikan batas awal dan akhir untuk dekomposisi
#Misalkan size = 4 maka proses 0 menghitung 0-25, proses 1 menghitung 26-50, dst
def local_loop(num_steps,begin,end):
    step = 1.0/num_steps
    sum = 0
    #4/(1+x^2)
    for i in range(begin,end):
        x = (i+0.5)*step
        sum = sum + 4.0/(1.0+x*x)
    return sum

#Fungsi Pi
def Pi(num_steps):  
    #Membuat COMM
    comm = MPI.COMM_WORLD
    
    #Mendapatkan rank proses
    rank = comm.Get_rank()
    
    #Mendapatkan total proses berjalan
    size = comm.Get_size()
    
    #Membuat variabel baru yang merupakan num_steps/total proses
    total_steps_process = num_steps/size
    
    #Mencari local_sum
    #Local_sum merupakan hasil dari memanggil fungsi local_loop
    begin = int(rank*total_steps_process)
    end = int((rank+1)*total_steps_process)
    local_sum = local_loop(num_steps, begin, end)
    
    #Melakukan penjumlahan dari local_sum proses-proses yang ada ke proses 0
    #Bisa digunakan reduce atau p2p sum
    sum = comm.allreduce(local_sum, op=MPI.SUM)
    
    print('===========================================================================')
    print('Proses untuk rank ', rank)
    print('Step yang diproses ', begin, '-', end-1)
    print('Nilai Local Sum = ', local_sum)
    
    #Jika saya proses dengan rank 0  maka tampilkan hasilnya
    if rank == 0:
        pi = sum / num_steps
        print(pi)
    
#Memanggil fungsi utama    
if __name__ == '__main__':
    Pi(10000)