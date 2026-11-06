# Original file
original = "original.pdf"
npages = 312 # Number of pages in original
oddpages = [
    # Odd-numbered pages to be replaced in original.
    # Will also replace each even page that follows one of these.
    7, 9, 11, 13, 15, 17, 21, 25, 27, 69, 73, 77, 101, 107, 125, 135,
    147, 149, 153, 159, 161, 171, 181, 183, 185, 203, 265, 279, 289
]
#
pages = sorted(oddpages + [o + 1 for o in oddpages]) # all pages to be replaced

# Revised file.
# It contains len(pages) pages, to replace corresponding pages in original.
revised = "revised.pdf" # snipped so that it only contains replacement pages

# Output file
outfile = "junk.pdf"

# pdftk command
pdftk = "%s O=%s R=%s " % ("pdftk.exe", original, revised)




# Build command to extract original pages to be replaced, for verification
pagelist = ""
for p in pages:
    pagelist += "O%d " % p
cmd = pdftk + "cat " + pagelist + "output %s" % outfile
print(cmd) # cut/paste screen output into shell or cmd

# Build command to replace original pages with revised
pagelist = ""
r = 1
for o in range(1, npages + 1):
    if o not in pages:
        pagelist += "O%d " % o
    else:
        pagelist += "R%d " % r
        r += 1
cmd = pdftk + "cat " + pagelist + "output %s" % outfile
print(cmd) # cut/paste screen output into shell or cmd


### Get pages in original that need replacing
##with open(oddfile) as fin:
##    o = [int(x) for x in fin]  # 0dd pages to replace
##e = [x + 1 for x in o] # even pages to replace
##pages = sorted(o + e) # all pages to replace

##def fred(pages):
##    s = set(pages)
##    hi = sorted(s.difference(set(n - 1 for n in s)))
##    lo = sorted(s.difference(set(n + 1 for n in s)))
##    return list(zip(lo, hi))
##    
##
##with open(oddfile) as fin:
##    o = [int(x) for x in fin]
##e = [x + 1 for x in o]
##swap_pages = set(o + e)
##keep_pages = set(range(1, npages+1)).difference(swap_pages)
##ranges = fred(keep_pages)
##nranges = len(ranges)
##gaps = [ranges[k][0] - ranges[k-1][1] - 1 for k in range(1, nranges)]
##
##print("pdftk.exe O=original.pdf R=revised.pdf cat ", end=" ")
##kk = 0
##for k in range(nranges - 1):
##    print("O%d-%d " % ranges[k], end=" ")
##    lo = kk + 1
##    hi = kk + gaps[k]
##    print("R%d-%d " % (lo, hi), end=" ")
##    kk = hi
##print("O%d-%d " % ranges[-1], end=" ")
##print("output junk.pdf")
##
##
####swap_ranges = fred(swap_pages)
##
####n = len(keep_ranges)
####assert len(swap_ranges) == n - 1
####
####for k in range(n - 1):
####    #lo, hi = keep_ranges[k]
####    print("O%d-%d " % keep_ranges[k], end=" ")
####print()
##    
##    
