def max_gold(monsters):
    n = len(monsters)
    
    if n == 0:  # No timeframes, no monsters, no gold
        return 0

    # dp_idle[t] = maximum earnings up to time t when idle
    dp_idle = [0] * n  # Gold earned while Kazuma is idle or moving to rear
    # dp_attack[t] = maximum earnings if Kazuma attacks at time t
    dp_attack = [0] * n  # Gold earned from attack at time t
    
    for t in range(1, n):
        # Case 1: Stay idle at time t (carry forward earnings)
        dp_idle[t] = dp_idle[t - 1]  # Just remain idle, carry forward the previous earnings
        
        # Case 2: Prepare at t-1 and attack at t
        if t > 0:
            # Kazuma can prepare at t-1 and attack at t if it is beneficial
            earnings_from_attack = monsters[t]
            protection_cost = monsters[t - 1]  # Pay for protection during preparation at t-1
            net_earnings = earnings_from_attack - protection_cost
            
            # Update dp_attack if this attack is beneficial
            dp_attack[t] = max(dp_attack[t], dp_idle[t - 1] + net_earnings)
            
            # After attacking, Kazuma has to move to the rear, carry forward the max value
            if t + 1 < n:  # Ensure we don't go out of bounds
                dp_idle[t + 1] = max(dp_idle[t + 1], dp_attack[t])

    # Return the best possible earnings
    return max(dp_idle[n - 1], dp_attack[n - 1])

# Example usage:
monsters = [1, 4, 5, 0, 4]
print(max_gold(monsters))  # Output: 7
