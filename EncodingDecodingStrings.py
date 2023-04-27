""" https://leetcode.com/problems/encode-and-decode-strings/solution/ & https://www.lintcode.com/problem/659/
Approach : This approach is based on the encoding used in HTTP v1.1. 
It doesn't depend on the set of input characters, and hence is more versatile.
Data stream is divided into chunks. Each chunk is preceded by its size in bytes.
ENCODING :
Iterate over the array of chunks, i.e. strings. For each chunk compute its length, and convert that length into 4-bytes string.
Append to encoded string : 4-bytes string with information about chunk size in bytes. Chunk itself. Return encoded string.
DECODING :
Iterate over the encoded string with a pointer i initiated as 0. While i < n:
Read 4 bytes s[i: i + 4]. It's chunk size in bytes. Convert this 4-bytes string to integer length. Move the pointer by 4 bytes i += 4.
Append to the decoded array string s[i: i + length]. Move the pointer by length bytes i += length. Return decoded array of strings.
"""
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output