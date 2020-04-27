#Import mpi4py
from mpi4py import MPI

#Membuat COMM
comm = MPI.COMM_WORLD

#Mendapatkan rank proses
rank = comm.Get_rank()

#Mendapatkan total proses berjalan
size = comm.Get_size()

#Jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    sended_messages = "Sistem Paralel dan Terdistribusi"
    print('===========================================================================')
    print('Proses untuk rank', rank)
    comm.bcast(sended_messages, root = 0)
    for higher_rank in range(1, size):
        print('rank', rank, 'membroadcast pesan', sended_messages, 'ke rank', higher_rank)

#Jika saya bukan rank 0 maka saya menerima pesan
else:
    received_messages = comm.bcast('', root = 0)
    lowest_rank = 0
    print('===========================================================================')
    print('Proses untuk rank', rank)
    print('rank', rank, 'mensubscribe pesan', received_messages, 'dari rank', lowest_rank)
