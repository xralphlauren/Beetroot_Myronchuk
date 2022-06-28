def rev(st):
    if len(st.split(' ')) == 1:
        return st
    return st.rsplit(' ', maxsplit=1)[1] + ' ' + rev(st.rsplit(' ', maxsplit=1)[0])


assert rev('магистр Йода так говорит поскольку джедай') == 'джедай поскольку говорит так Йода магистр'
