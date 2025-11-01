def shailesh_triplet(N):

    if N % 2 != 0:
        return "-1"
    
    if N == 2:
        return "-1"
    

    A = 1
    target_xor = N ^ 1  
    target_sum = 2 * N - 1 
    

    
    if (target_sum + target_xor) % 2 != 0:
        return "-1"
    
    B = (target_sum + target_xor) // 2
    C = (target_sum - target_xor) // 2
    
    if B <= 0 or C <= 0 or B == C or A == B or A == C:
        return "-1"
    
    if A + B + C == 2 * N and (A ^ B ^ C) == N:
        return f"{A} {B} {C}"
    
    return "-1"

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(shailesh_triplet(N))

if __name__ == "__main__":
    main()