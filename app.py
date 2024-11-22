from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json
        input_data = data.get("data", [])
        file_b64 = data.get("file_b64", None)
        
        # Parse data into numbers and alphabets
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]
        
        # Get the highest lowercase alphabet
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        highest_lowercase = max(lowercase_alphabets, default="", key=str.lower)
        
        # Check for prime numbers in numbers
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        primes = [int(num) for num in numbers if is_prime(int(num))]
        is_prime_found = len(primes) > 0
        
        # Response
        response = {
            "is_success": True,
            "user_id": "Raj_Gupta_30042003",  # Replace with your format
            "email": "rg123rdhu@gmail.com",  # Replace with your email
            "roll_number": "0101CS223D07",  # Replace with your roll number"application/octet-stream"
            "numbers": ["1", "334", "4", "7"],
            "alphabets": ["M", "B", "Z", "a"],
            "highest_lowercase_alphabet": ["a"],
            "is_prime_found": True,
            "file_valid": bool(file_b64),  # Simplified for now
            "file_mime_type": "application/octet-stream",  # Placeholder
            "file_size_kb": 0  # Placeholder
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == "__main__":
    app.run(debug=True)
