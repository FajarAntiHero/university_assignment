import module as m

def main() -> None:
    m.clearTerminal()
    garis = m.garis
    garis.duaGaris(100)
    m.mainTitle("program hitung pengeluaran dan pemasukkan")
    garis.duaGaris(100)
    print("")
    m.mainTitle("mode perhitungan")
    m.mainTitle("[OUT/out] or [IN/in]")
    print("")
    garis.duaGaris(100)
    inputMode = m.inputMode()

    match inputMode:
        case "out" : m.countOut()
        case "in" : pass
    pass

if __name__ == "__main__":
    main()