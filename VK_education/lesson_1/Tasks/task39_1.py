str = input()
str = str.lower()
st = set()
for i in str:
    if i != ' ':
        st.add(i)
print(" ".join(sorted(st)))
