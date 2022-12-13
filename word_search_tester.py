from word_search import *

# AN IMPORTANT TESTING NOTE OFF THE BAT.
# THE FUNCTIONS AT THE END OF THIS TEST (STARTING AT FILL_BLANKS) ARE NOT EXPTECTED TO MATCH EXACTLY.
# YOU WILL HAVE TO LOOK AT THE RESUTLS AND MANUALLY DECIDE IF THEY DO WHAT THE PROBLEM ASKED FOR...

unanswered='''
answer
'''

if Question1 == unanswered:
    print("Question 1 is unanswered! you should get on that!")
if Question2 == unanswered:
    print("Question 2 is unanswered! you should get on that!")
if Question3 == unanswered:
    print("Question 3 is unanswered! you should get on that!")
if Question4 == unanswered:
    print("Question 4 is unanswered! you should get on that!")

emptyish = [['x']]
g1 = [['a', 'b', 'c'], ['c', 'd', 'q']]
g2 = [['p', 'c', 'n', 'd', 't', 'h', 'g'],
      ['w', 'a', 'x', 'o', 'a', 'x', 'f'],
      ['o', 't', 'w', 'g', 'd', 'r', 'k'],
      ['l', 'j', 'p', 'i', 'b', 'e', 't'],
      ['f', 'v', 'l', 't', 'o', 'w', 'n']]
big = [['r', 'k', 's', 'a', 'j', 'p', 'k', 'c', 'o', 'x', 'e', 'c', 'd', 'r', 't', 'b', 'h', 'g', 't', 'v', 't', 'u', 't', 'k', 'y', 'w', 's', 'e', 'w', 'q', 'z', 'v', 'w', 'f', 'c', 'e', 'h', 's', 'd', 'g'],
       ['l', 'e', 'g', 'o', 'p', 'm', 'w', 'b', 'g', 'k', 'z', 'p', 'j', 'd', 'v', 'd', 'r', 'x', 'x', 'f',
        'y', 'n', 's', 'v', 'y', 'h', 'n', 'j', 'a', 'e', 'm', 'v', 't', 'c', 'l', 'e', 'w', 'l', 'x', 's'],
       ['v', 'j', 'q', 'd', 'z', 'u', 'b', 'h', 'u', 'a', 'p', 'b', 'm', 'f', 'n', 'd', 'd', 'z', 'l', 'u',
        'x', 'n', 'n', 'b', 'v', 's', 'k', 'e', 'j', 'v', 'y', 'a', 's', 'g', 'r', 'i', 'q', 'i', 'z', 'j'],
       ['u', 'm', 'v', 'a', 'q', 'f', 'i', 't', 's', 'z', 'z', 'z', 'u', 'c', 'c', 'o', 'n', 'r', 'i', 'k',
       'w', 'd', 'l', 'u', 'o', 't', 'q', 'f', 'q', 's', 'n', 'k', 'n', 's', 'b', 'b', 'v', 'o', 'd', 'd'],
       ['b', 'w', 'n', 'k', 'm', 'h', 'i', 'a', 's', 'o', 'x', 'g', 'c', 'l', 'o', 't', 't', 'h', 't', 'e',
       't', 't', 'b', 'c', 'j', 'w', 'c', 'f', 'r', 'f', 'n', 'r', 'j', 'o', 't', 'q', 'u', 'e', 'm', 'm'],
       ['i', 'l', 'n', 'r', 'c', 'i', 'j', 'u', 'v', 'y', 'k', 'i', 'n', 'h', 'g', 'i', 'h', 'g', 'm', 'i',
       'g', 'd', 'v', 'm', 'i', 'v', 'o', 'g', 'n', 'w', 'w', 'k', 'y', 'b', 'b', 'r', 'u', 'x', 'm', 'q'],
       ['m', 'e', 's', 'b', 'e', 'r', 'r', 'e', 'g', 'd', 'h', 'w', 'u', 'z', 'm', 'i', 'n', 'p', 'r', 'b',
       'r', 'm', 'f', 'v', 'i', 'q', 'k', 'p', 'h', 'f', 'u', 'm', 't', 's', 'u', 'a', 's', 'm', 'p', 'p'],
       ['k', 'g', 'a', 'l', 'x', 'b', 'i', 'b', 'j', 'e', 'i', 'j', 'g', 'e', 'k', 'c', 'm', 'm', 'a', 'a',
       'q', 't', 'j', 's', 'o', 'x', 'b', 'j', 'u', 'f', 'q', 'j', 's', 't', 'f', 'o', 't', 'c', 'g', 'm'],
       ['z', 'i', 'v', 'b', 's', 'g', 'g', 'z', 'e', 'w', 's', 'i', 'a', 'q', 'm', 'a', 'j', 't', 'a', 'u',
       'z', 'o', 'y', 'j', 'q', 'p', 'c', 'f', 'c', 'i', 's', 'i', 'n', 'f', 'x', 'i', 'x', 'y', 'f', 'a'],
       ['b', 'y', 'y', 'w', 'q', 'e', 'h', 'v', 'z', 'j', 'b', 'a', 'e', 'v', 'w', 'g', 'l', 'b', 'f', 'l',
       'p', 'u', 's', 'e', 'c', 's', 'c', 't', 'e', 'b', 'm', 'n', 'i', 'l', 'w', 'c', 'x', 'y', 'u', 'g'],
       ['z', 'l', 'n', 't', 'n', 'c', 't', 'g', 'q', 'r', 'i', 'q', 'q', 'q', 'u', 'k', 'x', 'i', 't', 'r',
       'w', 'p', 'r', 'w', 'o', 'r', 'z', 'o', 'b', 't', 'e', 'z', 'd', 'w', 'e', 'e', 'e', 'c', 'x', 'g'],
       ['l', 'v', 'b', 'w', 'q', 'p', 'g', 'z', 'h', 'u', 'i', 'y', 'b', 'x', 'y', 'q', 't', 'v', 'i', 'c',
       'u', 'r', 'l', 'h', 'x', 'k', 'g', 'b', 'e', 'e', 'k', 'k', 'd', 'r', 'x', 'z', 'h', 't', 'i', 'y'],
       ['t', 'h', 'c', 'y', 'i', 'i', 'z', 'g', 'm', 'p', 'd', 'n', 'c', 'x', 'w', 'h', 'y', 'i', 'i', 'f',
       'q', 'b', 't', 'e', 'b', 'a', 'o', 'z', 'n', 'l', 'f', 'v', 's', 'p', 'r', 's', 'm', 'g', 'z', 'i'],
       ['f', 's', 'a', 'v', 'z', 'v', 'r', 'l', 'q', 'l', 'b', 'q', 'n', 'a', 'd', 'e', 'q', 'q', 'q', 'w',
       'g', 'w', 'z', 'e', 'o', 'm', 's', 'h', 'n', 'w', 'b', 'j', 'g', 'a', 's', 'c', 'h', 'p', 'z', 'j'],
       ['l', 'o', 'c', 'j', 'r', 'j', 's', 'x', 'g', 'i', 'v', 's', 'j', 'j', 'w', 'n', 'e', 'c', 'i', 'n',
       'r', 't', 'x', 's', 'h', 'l', 'k', 'x', 'c', 'g', 'v', 'h', 'z', 'p', 'z', 'm', 't', 'l', 'c', 'l'],
       ['b', 'i', 'p', 'w', 'k', 'v', 'u', 'o', 'v', 'e', 'z', 'j', 'n', 'e', 'x', 'z', 't', 'i', 'd', 'm',
       'c', 'f', 'a', 'n', 'x', 'c', 'u', 'k', 'z', 'w', 't', 'y', 'n', 'f', 'z', 'q', 'j', 'x', 'd', 'k'],
       ['m', 'p', 'n', 'g', 'l', 'o', 'i', 'e', 't', 'u', 'l', 'o', 'r', 'r', 'z', 't', 'z', 'i', 'o', 'r',
       'm', 'p', 'q', 'v', 'a', 'h', 'z', 's', 'r', 'l', 'o', 'i', 'g', 'y', 'p', 'e', 's', 'x', 'p', 'x'],
       ['g', 'f', 'c', 'l', 'u', 'g', 'k', 'h', 'b', 'e', 'o', 'm', 't', 's', 'l', 'n', 'd', 'l', 'w', 'v',
       'r', 'q', 'c', 's', 'h', 'a', 'm', 'j', 'h', 'g', 'e', 'f', 'i', 'b', 's', 'n', 'j', 'p', 'g', 'f'],
       ['r', 'm', 'h', 'e', 'r', 'f', 'c', 'e', 'y', 'y', 'r', 'f', 'p', 'z', 's', 't', 'g', 'j', 't', 'l',
       'b', 'n', 'y', 'a', 'y', 'j', 'e', 'i', 'h', 'o', 'a', 'w', 'u', 'u', 'z', 'i', 'j', 'r', 'j', 'o'],
       ['y', 'o', 'q', 'g', 'r', 'p', 'm', 'g', 'h', 'c', 'v', 'p', 'h', 'e', 't', 'x', 'j', 'x', 't', 'l',
       'm', 'v', 'k', 'f', 'z', 'e', 'g', 'r', 'd', 'k', 'p', 'j', 'o', 'u', 'k', 'f', 'c', 'e', 'h', 'h'],
       ['q', 'x', 'u', 'a', 'c', 'z', 'p', 'x', 'p', 'a', 'y', 'q', 'h', 'o', 'x', 'i', 'x', 'b', 'p', 'w',
       's', 'n', 'l', 'q', 'r', 'q', 'd', 'y', 'm', 'j', 'm', 'h', 'l', 'e', 'a', 'r', 'n', 'v', 'l', 'p'],
       ['f', 'p', 'p', 's', 'o', 'o', 'y', 'v', 'j', 'b', 'a', 'f', 't', 'h', 'b', 'w', 'r', 'f', 't', 'w',
       'p', 't', 'o', 'i', 'o', 'l', 'v', 'o', 't', 'm', 'b', 'v', 'j', 't', 'c', 'm', 'i', 'o', 'j', 'b'],
       ['p', 'n', 'l', 'c', 't', 'e', 'c', 'p', 'i', 'm', 'o', 'g', 'p', 'j', 'x', 'j', 't', 'o', 't', 'x',
       'l', 'z', 'n', 'd', 'b', 'f', 'g', 'z', 't', 'p', 'p', 'l', 'a', 'c', 'w', 'w', 'n', 's', 'w', 'o'],
       ['t', 'j', 'y', 'f', 'c', 'f', 'w', 'n', 'k', 'd', 'v', 'q', 'm', 'x', 't', 'l', 'h', 'a', 'b', 't',
       'y', 'j', 'g', 'f', 'v', 'i', 's', 'a', 'n', 'c', 'r', 'p', 'x', 'e', 'e', 'p', 'o', 'j', 'g', 'f'],
       ['j', 'z', 'k', 't', 'w', 'l', 'p', 'c', 's', 's', 'k', 's', 'p', 'x', 'q', 's', 'o', 'm', 'e', 'c',
       'p', 'u', 'n', 'y', 'u', 'e', 'd', 'i', 'r', 'a', 'g', 'y', 'a', 'b', 'l', 'c', 'x', 'd', 'z', 'v'],
       ['l', 'r', 'i', 'd', 'y', 'p', 'e', 'a', 'q', 'n', 'd', 'f', 'e', 'y', 'e', 'o', 'z', 'a', 'p', 's',
       'p', 'k', 'e', 'y', 'l', 'n', 'a', 'r', 'd', 'b', 'h', 't', 'l', 'u', 'j', 'p', 'v', 'h', 'b', 'g'],
       ['l', 'y', 't', 'n', 'v', 'l', 'p', 's', 'b', 'i', 'w', 'u', 'k', 'm', 'a', 'p', 'j', 'x', 'b', 'v',
       'y', 's', 'm', 'm', 'i', 'r', 'k', 'a', 'q', 'b', 'u', 'v', 'i', 'v', 'm', 'e', 'o', 'j', 'r', 'b'],
       ['h', 'w', 'b', 'n', 'g', 'g', 'n', 'f', 'o', 'y', 'x', 'l', 'k', 'w', 'y', 'c', 'n', 't', 'd', 'h',
       't', 'w', 'i', 'k', 'e', 'x', 'd', 'u', 'n', 'd', 'x', 'a', 'e', 'c', 'o', 'y', 'g', 'e', 'v', 'w'],
       ['w', 'e', 'h', 'z', 'f', 'f', 'a', 'o', 'k', 'h', 'e', 'y', 'k', 'd', 'i', 'p', 'm', 'a', 'p', 'l',
       'p', 'i', 's', 'b', 'n', 'u', 'l', 'r', 'k', 'h', 'w', 'c', 'g', 'h', 'f', 'c', 'i', 'h', 'p', 'a'],
       ['u', 'l', 's', 'q', 'l', 'b', 'j', 'm', 'n', 'f', 'a', 'f', 'q', 'e', 'd', 'd', 'j', 'w', 'a', 'd',
       'e', 'o', 'd', 'r', 'p', 'd', 's', 'x', 'k', 'm', 'm', 'i', 'b', 'a', 'w', 'o', 'i', 'o', 'h', 'g'],
       ['t', 'x', 'p', 'l', 'v', 'y', 'e', 'c', 'i', 'l', 's', 'r', 'd', 'h', 'x', 't', 'j', 'p', 's', 'g',
       'e', 'j', 'n', 'o', 'g', 'e', 'y', 'y', 'd', 'n', 'f', 'i', 'u', 'l', 'z', 'y', 'k', 'h', 'l', 'm'],
       ['c', 'p', 'w', 'o', 'a', 'n', 'f', 'r', 'v', 'a', 'a', 'h', 'l', 'c', 'f', 'u', 'h', 'g', 'p', 'j',
       'k', 'p', 'o', 'd', 'n', 'b', 'p', 'b', 'b', 'p', 'p', 'g', 'z', 'p', 'o', 's', 'x', 'n', 'd', 'g'],
       ['t', 'v', 'z', 'r', 't', 'c', 'k', 'y', 's', 'm', 'l', 'd', 'u', 'q', 'f', 'e', 'k', 'w', 'r', 'o',
       'h', 'f', 'y', 'e', 'i', 'w', 'v', 'b', 'g', 'k', 'h', 'o', 'f', 'j', 'i', 'd', 'x', 'h', 't', 'm'],
       ['i', 'b', 'p', 'w', 'o', 'i', 'k', 'a', 'a', 't', 'h', 'a', 'o', 'q', 'o', 'w', 'n', 'x', 't', 'r',
       'j', 'q', 'v', 'u', 'z', 'a', 'j', 'l', 'i', 'k', 'f', 'z', 'w', 'r', 'a', 'd', 'x', 'i', 'e', 'q'],
       ['v', 'j', 'u', 'x', 'a', 'b', 'c', 'n', 'b', 'r', 'd', 'z', 'h', 'e', 'b', 'd', 'x', 'w', 'w', 'c',
       'v', 'a', 'e', 'k', 'p', 's', 'b', 'z', 'q', 's', 'a', 'o', 'q', 's', 'k', 'n', 'q', 'h', 'b', 'p'],
       ['m', 'v', 'i', 'c', 'g', 'x', 'y', 'f', 'i', 'e', 'q', 'w', 's', 'd', 'r', 'o', 'g', 'y', 's', 'o',
       'e', 'r', 'i', 'g', 'j', 'k', 'p', 'm', 'a', 't', 'n', 'x', 'o', 'a', 'o', 'l', 'g', 'k', 'c', 'r'],
       ['l', 'i', 'p', 'z', 'g', 'e', 'w', 'k', 'c', 'q', 'a', 's', 'e', 'n', 'e', 'a', 'g', 'j', 'i', 'o',
       't', 'a', 'q', 'j', 'n', 'i', 'x', 'd', 'p', 'h', 'u', 'k', 'k', 'h', 'u', 't', 'x', 'v', 'm', 'u'],
       ['e', 'f', 'u', 'm', 'v', 'p', 'r', 'r', 'x', 'j', 'p', 'o', 'i', 'x', 'r', 'i', 'c', 'q', 'v', 'b',
       'n', 's', 'p', 'a', 'k', 'n', 'o', 'w', 'j', 'h', 'p', 'y', 'y', 'v', 'o', 'p', 'h', 'n', 't', 'g'],
       ['n', 'c', 'i', 'v', 'u', 'z', 'i', 'x', 'm', 'i', 'u', 'e', 'c', 'm', 'i', 'v', 'q', 'r', 'u', 'o',
       'c', 'l', 'c', 'c', 'l', 'z', 'h', 'p', 'c', 'o', 'z', 'j', 'i', 'j', 'f', 's', 'j', 'e', 'n', 'i'],
       ['z', 'b', 'g', 'c', 'd', 'j', 'r', 'n', 'f', 'f', 'a', 'r', 'e', 'k', 'u', 'p', 'w', 'a', 'b', 'x', 'd', 'y', 'c', 'j', 'b', 'j', 'p', 'x', 'q', 'm', 'x', 'i', 'v', 'v', 'm', 'v', 'q', 'o', 'r', 'a']]

print("Testing get_size()")
print()
print(get_size(emptyish)) #(1, 1)
print(get_size(g1))       # (3, 2)
print(get_size(g2))       # (7, 5)
print(get_size(big))      # (40, 40)

print()
print("Testing print_word_grid()")
print()
print_word_grid(emptyish)
# x

print_word_grid(g1)
# abc
# cdq
# (this should print a newline at the end so the next grid doesn't start ont he same line)
print_word_grid(g2)
# pcndthg
# waxoaxf
# otwgdrk
# ljpibet
# fvltown
# (this should print a newline at the end so the next grid doesn't start ont he same line)

print_word_grid(big)
# rksajpkcoxecdrtbhgtvtutkywsewqzvwfcehsdg
# legopmwbgkzpjdvdrxxfynsvyhnjaemvtclewlxs
# vjqdzubhuapbmfnddzluxnnbvskejvyasgriqizj
# umvaqfitszzzucconrikwdluotqfqsnknsbbvodd
# bwnkmhiasoxgclotthtettbcjwcfrfnrjotquemm
# ilnrcijuvykinhgihgmigdvmivognwwkybbruxmq
# mesberregdhwuzminprbrmfviqkphfumtsuasmpp
# kgalxbibjeijgekcmmaaqtjsoxbjufqjstfotcgm
# zivbsggzewsiaqmajtauzoyjqpcfcisinfxixyfa
# byywqehvzjbaevwglbflpusecsctebmnilwcxyug
# zlntnctgqriqqqukxitrwprworzobtezdweeecxg
# lvbwqpgzhuiybxyqtvicurlhxkgbeekkdrxzhtiy
# thcyiizgmpdncxwhyiifqbtebaoznlfvsprsmgzi
# fsavzvrlqlbqnadeqqqwgwzeomshnwbjgaschpzj
# locjrjsxgivsjjwnecinrtxshlkxcgvhzpzmtlcl
# bipwkvuovezjnexztidmcfanxcukzwtynfzqjxdk
# mpngloietulorrztziormpqvahzsrloigypesxpx
# gfclugkhbeomtslndlwvrqcshamjhgefibsnjpgf
# rmherfceyyrfpzstgjtlbnyayjeihoawuuzijrjo
# yoqgrpmghcvphetxjxtlmvkfzegrdkpjoukfcehh
# qxuaczpxpayqhoxixbpwsnlqrqdymjmhlearnvlp
# fppsooyvjbafthbwrftwptoiolvotmbvjtcmiojb
# pnlctecpimogpjxjtotxlzndbfgztpplacwwnswo
# tjyfcfwnkdvqmxtlhabtyjgfvisancrpxeepojgf
# jzktwlpcsskspxqsomecpunyuediragyablcxdzv
# lridypeaqndfeyeozapspkeylnardbhtlujpvhbg
# lytnvlpsbiwukmapjxbvysmmirkaqbuvivmeojrb
# hwbnggnfoyxlkwycntdhtwikexdundxaecoygevw
# wehzffaokheykdipmaplpisbnulrkhwcghfcihpa
# ulsqlbjmnfafqeddjwadeodrpdsxkmmibawoiohg
# txplvyecilsrdhxtjpsgejnogeyydnfiulzykhlm
# cpwoanfrvaahlcfuhgpjkpodnbpbbppgzposxndg
# tvzrtckysmlduqfekwrohfyeiwvbgkhofjidxhtm
# ibpwoikaathaoqownxtrjqvuzajlikfzwradxieq
# vjuxabcnbrdzhebdxwwcvaekpsbzqsaoqsknqhbp
# mvicgxyfieqwsdrogysoerigjkpmatnxoaolgkcr
# lipzgewkcqaseneagjiotaqjnixdphukkhutxvmu
# efumvprrxjpoixricqvbnspaknowjhpyyvophntg
# ncivuzixmiuecmivqruoclcclzhpcozjijfsjeni
# zbgcdjrnffarekupwabxdycjbjpxqmxivvmvqora
# (this should print a newline at the end so the next grid doesn't start ont he same line)

print()
print("Testing copy_word_grid")
print()
newg1 = copy_word_grid(g1)
print_word_grid(newg1)
# abc
# cdq

newg1[0][0] = 'z'
newg1[1][0] = 'z'
# You might want to test even more changes -- but most of the time if you things right this will be enough.
# The autograder does slightly more careful tests changing every position in the copied word grid and making sure it
# doesn't change the original word grid.
print_word_grid(newg1)
# zbc
# zdq

print_word_grid(g1)
# abc
# cdq

newg2 = copy_word_grid(g2)
print_word_grid(newg2)
# pcndthg
# waxoaxf
# otwgdrk
# ljpibet
# fvltown

newg2[-1][2] = 'c'
newg2[-1][3] = 'l'
print_word_grid(newg2)
# pcndthg
# waxoaxf
# otwgdrk
# ljpibet
# fvclown

print_word_grid(g2)
# pcndthg
# waxoaxf
# otwgdrk
# ljpibet
# fvltown

print()
print("Testing extract()")
print()
print(extract(emptyish, (2, 2), RIGHT, 2)) #
print(extract(g2, (0, 0), RIGHT, 4))       # pcnd
print(extract(g2, (0, 0), DOWN, 5))        # pwolf
print(extract(g2, (1, 3), RIGHT_UP, 3))    # jwo
print(extract(g2, (4, 2), RIGHT, 5))       # drk
print(extract(g2, (3, 2), RIGHT_UP, 5))    # gah
print(extract(g2, (5, 2), DOWN, 5))        # rew
print(extract(big, (3, 3), RIGHT, 33))     # aqfitszzzucconrikwdluotqfqsnknsbb
print(extract(big, (0, 39), RIGHT_UP, 40)) # zcuzgbkyvlaykmeshotwmncvxlszetmissbqvixg

print()
print("Testing find()")
print()
print(find(g2, "gah"))         # ((3, 2), (1, -1))
print(find(g2, "wcl"))         # None
print(find(big, "shot"))       # ((15, 24), (1, -1))
print(find(big, "qvixg"))      # ((35, 4), (1, -1))
print(find(big, 'nade'))       # ((12, 13), (1, 0))
print(find(big, 'lxnna'))      # ((35, 35), (1, 1))
print(find(big, 'mlch'))       # ((25, 13), (0, 1))
print(find(big, 'university')) # None
print(find(emptyish, 'data'))  # None

print()
print("Testing show_solution()")
print()
show_solution(g2, "gah")
# GAH can be found as below
# pcndtHg
# waxoAxf
# otwGdrk
# ljpibet
# fvltown

show_solution(big, "shot")
# SHOT can be found as below
# rksajpkcoxecdrtbhgtvtutkywsewqzvwfcehsdg
# legopmwbgkzpjdvdrxxfynsvyhnjaemvtclewlxs
# vjqdzubhuapbmfnddzluxnnbvskejvyasgriqizj
# umvaqfitszzzucconrikwdluotqfqsnknsbbvodd
# bwnkmhiasoxgclotthtettbcjwcfrfnrjotquemm
# ilnrcijuvykinhgihgmigdvmivognwwkybbruxmq
# mesberregdhwuzminprbrmfviqkphfumtsuasmpp
# kgalxbibjeijgekcmmaaqtjsoxbjufqjstfotcgm
# zivbsggzewsiaqmajtauzoyjqpcfcisinfxixyfa
# byywqehvzjbaevwglbflpusecsctebmnilwcxyug
# zlntnctgqriqqqukxitrwprworzobtezdweeecxg
# lvbwqpgzhuiybxyqtvicurlhxkgbeekkdrxzhtiy
# thcyiizgmpdncxwhyiifqbtebaoznlfvsprsmgzi
# fsavzvrlqlbqnadeqqqwgwzeomshnwbjgaschpzj
# locjrjsxgivsjjwnecinrtxshlkxcgvhzpzmtlcl
# bipwkvuovezjnexztidmcfanxcukzwtynfzqjxdk
# mpngloietulorrztziormpqvahzsrloigypesxpx
# gfclugkhbeomtslndlwvrqcshamjhgefibsnjpgf
# rmherfceyyrfpzstgjtlbnyayjeihoawuuzijrjo
# yoqgrpmghcvphetxjxtlmvkfzegrdkpjoukfcehh
# qxuaczpxpayqhoxixbpwsnlqrqdymjmhlearnvlp
# fppsooyvjbafthbwrfTwptoiolvotmbvjtcmiojb
# pnlctecpimogpjxjtOtxlzndbfgztpplacwwnswo
# tjyfcfwnkdvqmxtlHabtyjgfvisancrpxeepojgf
# jzktwlpcsskspxqSomecpunyuediragyablcxdzv
# lridypeaqndfeyeozapspkeylnardbhtlujpvhbg
# lytnvlpsbiwukmapjxbvysmmirkaqbuvivmeojrb
# hwbnggnfoyxlkwycntdhtwikexdundxaecoygevw
# wehzffaokheykdipmaplpisbnulrkhwcghfcihpa
# ulsqlbjmnfafqeddjwadeodrpdsxkmmibawoiohg
# txplvyecilsrdhxtjpsgejnogeyydnfiulzykhlm
# cpwoanfrvaahlcfuhgpjkpodnbpbbppgzposxndg
# tvzrtckysmlduqfekwrohfyeiwvbgkhofjidxhtm
# ibpwoikaathaoqownxtrjqvuzajlikfzwradxieq
# vjuxabcnbrdzhebdxwwcvaekpsbzqsaoqsknqhbp
# mvicgxyfieqwsdrogysoerigjkpmatnxoaolgkcr
# lipzgewkcqaseneagjiotaqjnixdphukkhutxvmu
# efumvprrxjpoixricqvbnspaknowjhpyyvophntg
# ncivuzixmiuecmivqruoclcclzhpcozjijfsjeni
# zbgcdjrnffarekupwabxdycjbjpxqmxivvmvqora

show_solution(g2, "town")
# TOWN can be found as below
# pcndthg
# waxoaxf
# otwgdrk
# ljpibet
# fvlTOWN

show_solution(g2, "work")
# work is not found in this word search

print()
print("Testing make_empty_grid()")
print()
res = make_empty_grid(10, 10)
# make some changes to help you see if you got the rows independent or not!
# Again -- you might want to be more thurough personally.
res[0][0] = 'A'
print_word_grid(res)
# A?????????
# ??????????
# ??????????
# ??????????
# ??????????
# ??????????
# ??????????
# ??????????
# ??????????
# ??????????

res = make_empty_grid(3, 11)
res[0][0] = 'A'
print_word_grid(res)
# A??
# ???
# ???
# ???
# ???
# ???
# ???
# ???
# ???
# ???
# ???

print_word_grid(make_empty_grid(1, 1))
# ?

print()
print("Testing can_add_word()")
print()
g3 = [['d', '?', '?', '?', '?'],
      ['?', 'o', 'r', 'a', 't'],
      ['?', '?', 'g', 'a', '?'],
      ['?', '?', 'c', '?', '?']]
g4 = [['w', 'o', 'r', '?'],
      ['a', '?', 'i', 'i'],
      ['?', 'l', '?', 'n'],
      ['?', '?', 'g', '?']]
print(can_add_word(g3, 'bat', (0, 1), (0, 1)))  # True
print(can_add_word(g3, 'bat', (2, 0), (1, 1)))  # True
print(can_add_word(g3, 'bat', (3, 2), (0, 1)))  # False
print(can_add_word(g4, 'want', (0, 0), (0, 1))) # True
print(can_add_word(g4, 'want', (0, 0), (1, 1))) # True
print(can_add_word(g4, 'work', (0, 0), (1, 0))) # True
print(can_add_word(g4, 'ring', (2, 0), (1, 0))) # False
print(can_add_word(g4, 'ring', (2, 0), (0, 1))) # True
print(can_add_word(g4, 'kind', (3, 0), (0, 1))) # True
print(can_add_word(g4, 'air', (0, 2), (1, -1))) # True

print()
print("Testing do_add_word()")
print()
do_add_word(g3, 'bat', (2, 0), (1, 1))
print(g3)
# [['d', '?', 'b', '?', '?'], ['?', 'o', 'r', 'a', 't'], ['?', '?', 'g', 'a', 't'], ['?', '?', 'c', '?', '?']]

do_add_word(g4, 'want', (0, 0), (0, 1))
print(g4)
# [['w', 'o', 'r', '?'], ['a', '?', 'i', 'i'], ['n', 'l', '?', 'n'], ['t', '?', 'g', '?']]

do_add_word(g4, 'kind', (3, 0), (0, 1))
print(g4)
# [['w', 'o', 'r', 'k'], ['a', '?', 'i', 'i'], ['n', 'l', '?', 'n'], ['t', '?', 'g', 'd']]

do_add_word(g4, 'only', (1, 0), (0, 1))
print(g4)
# [['w', 'o', 'r', 'k'], ['a', 'n', 'i', 'i'], ['n', 'l', '?', 'n'], ['t', 'y', 'g', 'd']]

do_add_word(g4, 'ring', (2, 0), (0, 1))
print(g4)
# [['w', 'o', 'r', 'k'], ['a', 'n', 'i', 'i'], ['n', 'l', 'n', 'n'], ['t', 'y', 'g', 'd']]

print_word_grid(g3)
# d?b??
# ?orat
# ??gat
# ??c??

print_word_grid(g4)
# work
# anii
# nlnn
# tygd

print()
print("Testing fill_blanks()")
print()
# FROM HERE ON IN -- THE TESTS ARE NOT EXPECTED TO MATCH EXACTLY!!!
# For tests here -- you want to check that question marks have been filled in, but the not-question-mark values have not been changed.
# you may find it helpful to add a print before the fill_grids if you're having trouble remembering the various grids

g5 = [['?', '?', '?', '?'],
      ['?', '?', '?', '?'],
      ['?', '?', '?', '?'],
      ['d', 'a', 't', 'a']]
fill_blanks(g3)
print_word_grid(g3)
fill_blanks(g5)
print_word_grid(g5)
fill_blanks(g2)
print_word_grid(g2)

print("Testing full! Get Ready!")
# Likewise, this one isn't expected to return the same thing each time -- but it should generally generate a complete solution
# with random-looking letters and all the right words being in the list!
print()
print(
    "Generating word search based on [java, python, list, set, tuple, string]: ")
print()
grid, words = generate(10, 10, ["java", "python", "list", "set", "tuple", "string"])
print_word_grid(grid)
for w in words:
    show_solution(grid, w)

grid, words = generate(3, 3, ['rat', 'ham', 'hi'])
for w in words:
    show_solution(grid, w)

'''
Testing get_size()

(1, 1)
(3, 2)
(7, 5)
(40, 40)

Testing print_word_grid()

x
abc
cdq
pcndthg
waxoaxf
otwgdrk
ljpibet
fvltown
rksajpkcoxecdrtbhgtvtutkywsewqzvwfcehsdg
legopmwbgkzpjdvdrxxfynsvyhnjaemvtclewlxs
vjqdzubhuapbmfnddzluxnnbvskejvyasgriqizj
umvaqfitszzzucconrikwdluotqfqsnknsbbvodd
bwnkmhiasoxgclotthtettbcjwcfrfnrjotquemm
ilnrcijuvykinhgihgmigdvmivognwwkybbruxmq
mesberregdhwuzminprbrmfviqkphfumtsuasmpp
kgalxbibjeijgekcmmaaqtjsoxbjufqjstfotcgm
zivbsggzewsiaqmajtauzoyjqpcfcisinfxixyfa
byywqehvzjbaevwglbflpusecsctebmnilwcxyug
zlntnctgqriqqqukxitrwprworzobtezdweeecxg
lvbwqpgzhuiybxyqtvicurlhxkgbeekkdrxzhtiy
thcyiizgmpdncxwhyiifqbtebaoznlfvsprsmgzi
fsavzvrlqlbqnadeqqqwgwzeomshnwbjgaschpzj
locjrjsxgivsjjwnecinrtxshlkxcgvhzpzmtlcl
bipwkvuovezjnexztidmcfanxcukzwtynfzqjxdk
mpngloietulorrztziormpqvahzsrloigypesxpx
gfclugkhbeomtslndlwvrqcshamjhgefibsnjpgf
rmherfceyyrfpzstgjtlbnyayjeihoawuuzijrjo
yoqgrpmghcvphetxjxtlmvkfzegrdkpjoukfcehh
qxuaczpxpayqhoxixbpwsnlqrqdymjmhlearnvlp
fppsooyvjbafthbwrftwptoiolvotmbvjtcmiojb
pnlctecpimogpjxjtotxlzndbfgztpplacwwnswo
tjyfcfwnkdvqmxtlhabtyjgfvisancrpxeepojgf
jzktwlpcsskspxqsomecpunyuediragyablcxdzv
lridypeaqndfeyeozapspkeylnardbhtlujpvhbg
lytnvlpsbiwukmapjxbvysmmirkaqbuvivmeojrb
hwbnggnfoyxlkwycntdhtwikexdundxaecoygevw
wehzffaokheykdipmaplpisbnulrkhwcghfcihpa
ulsqlbjmnfafqeddjwadeodrpdsxkmmibawoiohg
txplvyecilsrdhxtjpsgejnogeyydnfiulzykhlm
cpwoanfrvaahlcfuhgpjkpodnbpbbppgzposxndg
tvzrtckysmlduqfekwrohfyeiwvbgkhofjidxhtm
ibpwoikaathaoqownxtrjqvuzajlikfzwradxieq
vjuxabcnbrdzhebdxwwcvaekpsbzqsaoqsknqhbp
mvicgxyfieqwsdrogysoerigjkpmatnxoaolgkcr
lipzgewkcqaseneagjiotaqjnixdphukkhutxvmu
efumvprrxjpoixricqvbnspaknowjhpyyvophntg
ncivuzixmiuecmivqruoclcclzhpcozjijfsjeni
zbgcdjrnffarekupwabxdycjbjpxqmxivvmvqora

Testing copy_word_grid

abc
cdq
zbc
zdq
abc
cdq
pcndthg
waxoaxf
otwgdrk
ljpibet
fvltown
pcndthg
waxoaxf
otwgdrk
ljpibet
fvclown
pcndthg
waxoaxf
otwgdrk
ljpibet
fvltown

Testing extract()


pcnd
pwolf
jwo
drk
gah
rew
aqfitszzzucconrikwdluotqfqsnknsbb
zcuzgbkyvlaykmeshotwmncvxlszetmissbqvixg

Testing find()

((3, 2), (1, -1))
None
((15, 24), (1, -1))
((35, 4), (1, -1))
((12, 13), (1, 0))
((35, 35), (1, 1))
((25, 13), (0, 1))
None
None

Testing show_solution()

GAH can be found as below
pcndtHg
waxoAxf
otwGdrk
ljpibet
fvltown
SHOT can be found as below
rksajpkcoxecdrtbhgtvtutkywsewqzvwfcehsdg
legopmwbgkzpjdvdrxxfynsvyhnjaemvtclewlxs
vjqdzubhuapbmfnddzluxnnbvskejvyasgriqizj
umvaqfitszzzucconrikwdluotqfqsnknsbbvodd
bwnkmhiasoxgclotthtettbcjwcfrfnrjotquemm
ilnrcijuvykinhgihgmigdvmivognwwkybbruxmq
mesberregdhwuzminprbrmfviqkphfumtsuasmpp
kgalxbibjeijgekcmmaaqtjsoxbjufqjstfotcgm
zivbsggzewsiaqmajtauzoyjqpcfcisinfxixyfa
byywqehvzjbaevwglbflpusecsctebmnilwcxyug
zlntnctgqriqqqukxitrwprworzobtezdweeecxg
lvbwqpgzhuiybxyqtvicurlhxkgbeekkdrxzhtiy
thcyiizgmpdncxwhyiifqbtebaoznlfvsprsmgzi
fsavzvrlqlbqnadeqqqwgwzeomshnwbjgaschpzj
locjrjsxgivsjjwnecinrtxshlkxcgvhzpzmtlcl
bipwkvuovezjnexztidmcfanxcukzwtynfzqjxdk
mpngloietulorrztziormpqvahzsrloigypesxpx
gfclugkhbeomtslndlwvrqcshamjhgefibsnjpgf
rmherfceyyrfpzstgjtlbnyayjeihoawuuzijrjo
yoqgrpmghcvphetxjxtlmvkfzegrdkpjoukfcehh
qxuaczpxpayqhoxixbpwsnlqrqdymjmhlearnvlp
fppsooyvjbafthbwrfTwptoiolvotmbvjtcmiojb
pnlctecpimogpjxjtOtxlzndbfgztpplacwwnswo
tjyfcfwnkdvqmxtlHabtyjgfvisancrpxeepojgf
jzktwlpcsskspxqSomecpunyuediragyablcxdzv
lridypeaqndfeyeozapspkeylnardbhtlujpvhbg
lytnvlpsbiwukmapjxbvysmmirkaqbuvivmeojrb
hwbnggnfoyxlkwycntdhtwikexdundxaecoygevw
wehzffaokheykdipmaplpisbnulrkhwcghfcihpa
ulsqlbjmnfafqeddjwadeodrpdsxkmmibawoiohg
txplvyecilsrdhxtjpsgejnogeyydnfiulzykhlm
cpwoanfrvaahlcfuhgpjkpodnbpbbppgzposxndg
tvzrtckysmlduqfekwrohfyeiwvbgkhofjidxhtm
ibpwoikaathaoqownxtrjqvuzajlikfzwradxieq
vjuxabcnbrdzhebdxwwcvaekpsbzqsaoqsknqhbp
mvicgxyfieqwsdrogysoerigjkpmatnxoaolgkcr
lipzgewkcqaseneagjiotaqjnixdphukkhutxvmu
efumvprrxjpoixricqvbnspaknowjhpyyvophntg
ncivuzixmiuecmivqruoclcclzhpcozjijfsjeni
zbgcdjrnffarekupwabxdycjbjpxqmxivvmvqora
TOWN can be found as below
pcndthg
waxoaxf
otwgdrk
ljpibet
fvlTOWN
work is not found in this word search

Testing make_empty_grid()

A?????????
??????????
??????????
??????????
??????????
??????????
??????????
??????????
??????????
??????????
A??
???
???
???
???
???
???
???
???
???
???
?

Testing can_add_word()

True
True
False
True
True
True
False
True
True
True

Testing do_add_word()

[['d', '?', 'b', '?', '?'], ['?', 'o', 'r', 'a', 't'], ['?', '?', 'g', 'a', 't'], ['?', '?', 'c', '?', '?']]
[['w', 'o', 'r', '?'], ['a', '?', 'i', 'i'], ['n', 'l', '?', 'n'], ['t', '?', 'g', '?']]
[['w', 'o', 'r', 'k'], ['a', '?', 'i', 'i'], ['n', 'l', '?', 'n'], ['t', '?', 'g', 'd']]
[['w', 'o', 'r', 'k'], ['a', 'n', 'i', 'i'], ['n', 'l', '?', 'n'], ['t', 'y', 'g', 'd']]
[['w', 'o', 'r', 'k'], ['a', 'n', 'i', 'i'], ['n', 'l', 'n', 'n'], ['t', 'y', 'g', 'd']]
d?b??
?orat
??gat
??c??
work
anii
nlnn
tygd

Testing fill_blanks()

dfbrk
morat
kagat
ducni
oozo
zsld
qwwn
data
pcndthg
waxoaxf
otwgdrk
ljpibet
fvltown
Testing full! Get Ready!

Generating word search based on [java, python, list, set, tuple, string]: 

pdyhstring
gldmsbcwvs
iishpwkzjl
ksebndjvat
uttthakuvu
tsijgygzap
edgiiguobl
edgeqppcae
kskpythony
dpmazvjrej
JAVA can be found as below
pdyhstring
gldmsbcwvs
iishpwkzJl
ksebndjvAt
uttthakuVu
tsijgygzAp
edgiiguobl
edgeqppcae
kskpythony
dpmazvjrej
PYTHON can be found as below
pdyhstring
gldmsbcwvs
iishpwkzjl
ksebndjvat
uttthakuvu
tsijgygzap
edgiiguobl
edgeqppcae
kskPYTHONy
dpmazvjrej
LIST can be found as below
pdyhstring
gLdmsbcwvs
iIshpwkzjl
kSebndjvat
uTtthakuvu
tsijgygzap
edgiiguobl
edgeqppcae
kskpythony
dpmazvjrej
SET can be found as below
pdyhstring
gldmsbcwvs
iiShpwkzjl
ksEbndjvat
utTthakuvu
tsijgygzap
edgiiguobl
edgeqppcae
kskpythony
dpmazvjrej
TUPLE can be found as below
pdyhstring
gldmsbcwvs
iishpwkzjl
ksebndjvaT
uttthakuvU
tsijgygzaP
edgiiguobL
edgeqppcaE
kskpythony
dpmazvjrej
STRING can be found as below
pdyhSTRING
gldmsbcwvs
iishpwkzjl
ksebndjvat
uttthakuvu
tsijgygzap
edgiiguobl
edgeqppcae
kskpythony
dpmazvjrej
RAT can be found as below
RAT
ham
hiw
HAM can be found as below
rat
HAM
hiw
HI can be found as below
rat
Ham
hIw

'''
