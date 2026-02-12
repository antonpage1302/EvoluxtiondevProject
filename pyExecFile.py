#!/usr/bin/env python3

def generate_iframe(port: int, html_file: str = "index.html", width: int = 800, height: int = 600):
    """Generate iframe HTML code for localhost with a frame and footer"""
    return f"""
<div style="border:2px solid #000; padding:10px; display:inline-block;">
    <iframe src="http://localhost:{port}/{html_file}" width="{width}" height="{height}" style="display:block; border:none;"></iframe>
    <div style="text-align:center; margin-top:5px; font-size:12px;">
        Powered by <strong>Evoluxtion</strong> | 
        <a href="https://github.com/antonpage1302/antonpage1302.github.io" target="_blank">GitHub</a>
    </div>
</div>
""".strip()

if __name__ == "__main__":
    port_input = input("Enter the port where your local server will run: ").strip()
    if not port_input.isdigit():
        print("Invalid port. Please enter a number.")
        exit(1)
    port = int(port_input)

    html_file_input = input("Enter the HTML file name (default: index.html): ").strip()
    html_file = html_file_input if html_file_input else "index.html"

    iframe_code = generate_iframe(port, html_file)
    
    print("\nGenerated iframe code for localhost with branding:\n")
    print(iframe_code)
    print("\nYou can insert this code into your HTML file.")
