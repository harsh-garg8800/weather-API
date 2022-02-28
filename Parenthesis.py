class Solution:
   def isValid( self, sequence ):
       # Replace the proper pairs until sequence becomes empty or no pairs are present
       while True:
           if '()' in sequence :
               sequence = sequence.replace ( '()' , '' )
           elif '{}' in sequence :
               sequence = sequence.replace ( '{}' , '' )
           elif '[]' in sequence :
               sequence = sequence.replace ( '[]' , '' )
           else :
               return not sequence

if __name__ == '__main__':
   sequence = '([{}])'
   print(f'Is {sequence} valid: {Solution().isValid(sequence)}')

   sequence1 = '([]{})'
   print(f'Is {sequence1} valid: {Solution().isValid (sequence1)}')

   sequence2 = '([]{})'
   print(f'Is {sequence2} valid: {Solution().isValid (sequence2)}')

   sequence3 = '()[]{}'
   print(f'Is {sequence3} valid: {Solution().isValid (sequence3)}')

   sequence4 = '([)]'
   print(f'Is {sequence4} valid: {Solution().isValid (sequence4)}')

   sequence5 = '([]'
   print(f'Is {sequence5} valid: {Solution().isValid (sequence5)}')

   sequence6 = '[])'
   print(f'Is {sequence6} valid: {Solution().isValid (sequence6)}')

   sequence7 = '([})'
   print(f'Is {sequence7} valid: {Solution().isValid (sequence7)}')


