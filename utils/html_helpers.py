import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_index_html(output_dir):
    """
    Generates an index.html file that links to all the HTML reports in the output directory
    with a table structure to display the folder and file hierarchy.
    """
    # Create an index.html file
    index_file_path = os.path.join(output_dir, "index.html")
    with open(index_file_path, "w", encoding="utf-8") as index_file:
        # Start the HTML structure
        index_file.write("""
        <html>
        <head>
            <title>Code Scan Reports</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    padding: 8px;
                    text-align: left;
                    border: 1px solid #ddd;
                }
                th {
                    background-color: #f2f2f2;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Code Scan Reports</h1>
            <table>
                <tr>
                    <th>Folder</th>
                    <th>File</th>
                    <th>Link</th>
                </tr>
        """)

        # Walk through the output directory and create a table row for each HTML file
        for root, _, files in os.walk(output_dir):
            # Skip the root directory itself
            if root == output_dir:
                continue

            for file in files:
                if file.endswith(".html"):
                    # Get the folder and file name
                    folder = os.path.relpath(root, output_dir)
                    file_name = file

                    # Create the link to the HTML file (make filename a clickable link)
                    file_link = os.path.join(folder, file_name)

                    # Write the row to the index file
                    index_file.write(f"""
                    <tr>
                        <td>{folder}</td>
                        <td>{file_name}</td>
                        <td><a href="{file_link}">{file_name}</a></td>
                    </tr>
                    """)

        # Close the table and HTML structure
        index_file.write("""
            </table>
        </body>
        </html>
        """)

    print(f"{Fore.GREEN}Index file created at {index_file_path}{Style.RESET_ALL}")
