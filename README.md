# Walmart Sales Data Compression

This project explores three different custom algorithms to compress sales data from a **Walmart dataset**. The goal is to reduce the storage footprint of large Excel files by encoding numerical sequences into more compact formats.

## Performance Comparison

|  |  |  |  |
|----|----|----|----|
| **Method** | **File Size** | **Reduction** | **Logic Type** |
| **Original File** | **20.1 MB** | \- | Plain text/Excel standard |
| **Version 1** | **14.4 MB** | \~28% | Basic RLE (Run-Length Encoding) |
| **Version 2** | **13.3 MB** | **\~34%** | Base 52 Alpha-Encoding |
| **Version 3** | **13.3 MB** | **\~34%** | Global Pattern Tokenization |

------------------------------------------------------------------------

## 🛠️ Compression Methods

### 1. Version 1: Run-Length Encoding (RLE)

This is the foundational approach. Instead of storing repeated numbers individually (e.g., `5 5 5 5`), the algorithm stores the value and the count.

-   **Key Feature:** Uses a simple mapping (`zabcdefghi`) to represent the frequency of a number.

-   **Separation:** Uses spaces to distinguish between adjacent numerical values.

### 2. Version 2: Base 52 Alpha-Encoding

This version evolves the RLE logic by removing the need for spaces, which are "hidden" byte-wasters.

-   **Logic:** It maps frequencies to a **Base 52** system (a-z, A-Z).

-   **Efficiency:** By using letters as delimiters (e.g., `10c` instead of `10 10 10`), it packs more information into fewer characters, significantly dropping the size to 13.3 MB.

### 3. Version 3: Global Tokenization (Ultra-Storage)

Instead of looking at single number repetitions, this method analyzes the **entire dataset** to find recurring patterns of triplets (sequences of 3 numbers).

-   **Logic:** It identifies the 52 most frequent "sales patterns" and assigns each a unique single-character Token.

-   **Result:** It achieves high density by replacing long strings of data with a single letter, matching the efficiency of V2 but using a more structural data-mining approach.

------------------------------------------------------------------------

## 🚀 How to use

1.  Clone the repository.

2.  Create a virtual environment: `python3 -m venv .venv`.

3.  Install dependencies: `pip install pandas openpyxl`.

4.  Run the scripts to see the compression in action.
