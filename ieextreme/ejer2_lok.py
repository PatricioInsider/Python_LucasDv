def solve_bitonic_sequences(M):
    MOD = 10**9 + 7
   
    results = []
    
    for target in range(1, M + 1):
        
        dp_inc = {}
        
        for v in range(1, target + 1):
            if v <= target:
                dp_inc[(v, v)] = 1
        
        for s in range(1, target + 1):
            for last in range(1, s + 1):
                if (s, last) not in dp_inc:
                    continue
                count = dp_inc[(s, last)]
                
                for next_val in range(last + 1, target - s + 1):
                    new_sum = s + next_val
                    if new_sum <= target:
                        if (new_sum, next_val) not in dp_inc:
                            dp_inc[(new_sum, next_val)] = 0
                        dp_inc[(new_sum, next_val)] = (dp_inc[(new_sum, next_val)] + count) % MOD
        
        total = 0
        
        for (s, last), count in dp_inc.items():
            if s == target:
                total = (total + count) % MOD
        

        for (sum_inc, peak_val), count_inc in dp_inc.items():
            if sum_inc >= target:
                continue
            
            remaining = target - sum_inc

            dp_dec = {}
            
            # Base case
            for v in range(1, min(peak_val, remaining + 1)):
                dp_dec[(v, v)] = 1
            
            for s in range(1, remaining + 1):
                for last in range(1, min(peak_val, s + 1)):
                    if (s, last) not in dp_dec:
                        continue
                    cnt = dp_dec[(s, last)]
                    
                    for next_val in range(1, last):
                        new_sum = s + next_val
                        if new_sum <= remaining:
                            if (new_sum, next_val) not in dp_dec:
                                dp_dec[(new_sum, next_val)] = 0
                            dp_dec[(new_sum, next_val)] = (dp_dec[(new_sum, next_val)] + cnt) % MOD
            
            for (s, last), count_dec in dp_dec.items():
                if s == remaining:
                    total = (total + count_inc * count_dec) % MOD
        
        results.append(total)
    
    return results

M = int(input())

results = solve_bitonic_sequences(M)
print(' '.join(map(str, results)))
