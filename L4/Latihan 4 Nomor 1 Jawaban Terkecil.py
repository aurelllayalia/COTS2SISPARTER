#Import mpi4py
from mpi4py import MPI

#Membuat COMM
comm = MPI.COMM_WORLD

#Mendapatkan rank proses
rank = comm.Get_rank()

#Mendapatkan total proses berjalan
size = comm.Get_size()

#Jika saya rank ke 0 maka saya akan mengirimkan pesan ke proses yang mempunyai rank 1 s.d size
if rank == 0:
    sended_messages = "Sistem Paralel dan Terdistribusi Terkecil"
    print('===========================================================================')
    print('Proses untuk rank', rank, '(Rank Terkecil)')
    for higher_rank in range(1,size):
        comm.send(sended_messages, dest = higher_rank)
        print('rank', rank, 'mengirim pesan', sended_messages, 'ke rank', higher_rank)

#Jika saya bukan rank 0 maka saya menerima pesan yang berasal dari proses dengan rank 0
else:
    received_messages = comm.recv(source = 0)
    lowest_rank = 0
    print('===========================================================================')
    print('Proses untuk rank', rank)
    print('rank', rank, 'menerima pesan', received_messages, 'dari rank', lowest_rank)
