#!/usr/bin/env python3
"""
Google Cloud Run Free Tier Calculator
Estimate your usage against free tier limits
"""

def calculate_free_tier_usage():
    print("🧮 Google Cloud Run Free Tier Usage Calculator")
    print("=" * 50)
    
    # Free tier limits
    CPU_LIMIT = 180000  # vCPU-seconds per month
    MEMORY_LIMIT = 360000  # GiB-seconds per month
    REQUEST_LIMIT = 2000000  # requests per month
    NETWORK_LIMIT = 1  # GiB per month
    
    # Your app configuration
    CPU_ALLOCATION = 1  # vCPUs
    MEMORY_ALLOCATION = 0.5  # GiB (512 MiB)
    
    print(f"📊 Your Configuration:")
    print(f"   CPU: {CPU_ALLOCATION} vCPU")
    print(f"   Memory: {MEMORY_ALLOCATION} GiB")
    print(f"   Min Instances: 0 (scales to zero)")
    print(f"   Max Instances: 10")
    print()
    
    # Get user input for usage estimation
    try:
        print("📝 Estimate Your Usage:")
        avg_processing_time = float(input("   Average request processing time (seconds): "))
        monthly_requests = int(input("   Expected monthly requests: "))
        
        print()
        print("🔢 Calculations:")
        print("-" * 30)
        
        # Calculate resource usage
        total_cpu_seconds = monthly_requests * avg_processing_time * CPU_ALLOCATION
        total_memory_seconds = monthly_requests * avg_processing_time * MEMORY_ALLOCATION
        
        print(f"CPU Usage: {total_cpu_seconds:,.0f} vCPU-seconds")
        print(f"Memory Usage: {total_memory_seconds:,.0f} GiB-seconds")
        print(f"Request Count: {monthly_requests:,} requests")
        print()
        
        # Check against limits
        print("🎯 Free Tier Limit Check:")
        print("-" * 30)
        
        cpu_percent = (total_cpu_seconds / CPU_LIMIT) * 100
        memory_percent = (total_memory_seconds / MEMORY_LIMIT) * 100
        request_percent = (monthly_requests / REQUEST_LIMIT) * 100
        
        def status_icon(percent):
            if percent <= 50:
                return "✅"
            elif percent <= 80:
                return "⚠️"
            else:
                return "❌"
        
        print(f"{status_icon(cpu_percent)} CPU: {cpu_percent:.1f}% of limit ({total_cpu_seconds:,.0f}/{CPU_LIMIT:,})")
        print(f"{status_icon(memory_percent)} Memory: {memory_percent:.1f}% of limit ({total_memory_seconds:,.0f}/{MEMORY_LIMIT:,})")
        print(f"{status_icon(request_percent)} Requests: {request_percent:.1f}% of limit ({monthly_requests:,}/{REQUEST_LIMIT:,})")
        print()
        
        # Determine bottleneck
        bottleneck = "CPU" if cpu_percent >= memory_percent else "Memory"
        max_percent = max(cpu_percent, memory_percent, request_percent)
        
        if max_percent <= 100:
            print("🎉 RESULT: You're within the free tier limits!")
        else:
            print("⚠️ RESULT: You may exceed free tier limits.")
            print(f"   Bottleneck: {bottleneck} usage")
            
        print()
        print("💡 Free Tier Capacity:")
        print("-" * 30)
        
        # Calculate maximum requests within free tier
        max_requests_cpu = CPU_LIMIT // (avg_processing_time * CPU_ALLOCATION)
        max_requests_memory = MEMORY_LIMIT // (avg_processing_time * MEMORY_ALLOCATION)
        max_requests_limit = REQUEST_LIMIT
        
        max_requests = min(max_requests_cpu, max_requests_memory, max_requests_limit)
        
        print(f"Max monthly requests (free): {max_requests:,.0f}")
        print(f"Max daily requests (free): {max_requests/30:,.0f}")
        print(f"Max hourly requests (free): {max_requests/(30*24):,.0f}")
        
        # Cost estimation if exceeded
        if max_percent > 100:
            print()
            print("💰 Estimated Monthly Cost (if exceeded):")
            print("-" * 40)
            
            # Pricing (us-central1)
            CPU_PRICE = 0.000024  # per vCPU-second
            MEMORY_PRICE = 0.0000025  # per GiB-second
            REQUEST_PRICE = 0.40 / 1000000  # per request
            
            excess_cpu = max(0, total_cpu_seconds - CPU_LIMIT)
            excess_memory = max(0, total_memory_seconds - MEMORY_LIMIT)
            excess_requests = max(0, monthly_requests - REQUEST_LIMIT)
            
            cpu_cost = excess_cpu * CPU_PRICE
            memory_cost = excess_memory * MEMORY_PRICE
            request_cost = excess_requests * REQUEST_PRICE
            total_cost = cpu_cost + memory_cost + request_cost
            
            print(f"CPU overage cost: ${cpu_cost:.4f}")
            print(f"Memory overage cost: ${memory_cost:.4f}")
            print(f"Request overage cost: ${request_cost:.4f}")
            print(f"Total estimated cost: ${total_cost:.2f}")
            
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
    except KeyboardInterrupt:
        print("\n👋 Calculator exited.")

if __name__ == "__main__":
    calculate_free_tier_usage()
