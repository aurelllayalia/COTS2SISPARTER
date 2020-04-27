#Import mpi4py
from mpi4py import MPI

#Membuat COMM
comm = MPI.COMM_WORLD

#Mendapatkan rank proses
rank = comm.Get_rank()

#Mendapatkan total proses berjalan
size = comm.Get_size()

#Jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == size-1:
    sended_messages = "Sistem Paralel dan Terdistribusi Terbesar"
    print('===========================================================================')
    print('Proses untuk rank', rank, '(Rank terbesar)')
    for lower_rank in range(size-1):
        comm.send(sended_messages, dest = lower_rank)
        print('rank', rank, 'mengirim pesan', sended_messages, 'ke rank', lower_rank)

#Jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
    received_messages = comm.recv(source = size-1)
    highest_rank = size-1
    print('===========================================================================')
    print('Proses untuk rank', rank)
    print('rank', rank, 'menerima pesan', received_messages, 'dari rank', highest_rank)
