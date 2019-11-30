import math

print("Program for calculating the diameters of pipelines")

con = "Y"
while con == "Y":

    c = input("What pipeline (Suction/Pressure) and for what medium (Biogas/Wastewater/Sludge) would you like to calculate (e.g. SB => suction pipeline for biogas)? ")

    def v(v1, v2):
        global con
        try:
            q = float(input("What is the flow [m3/h]? "))
        except ValueError:
            print("Entered wrong flow value. Must be a number")
            con = input("Would like to do a new calculation? [Y/N] ")

        else:
            dl = []
            vl = []
            dn1 = [25, 50, 80, 100, 125, 150]
            dn2 = list(range(150,1000,50))
            dn = dn1 + dn2

            for d in dn:
                A = float(((d/2000) ** 2 * math.pi))
                V = round((q / A / 3600), 2)
                if V >= v1 and V <= v2:
                    vl.append(V)
                    dl.append(d)

            if dl == [] and vl == []:
                print("Entered flow value is out of range for normative DN.")
                con = input("Would like to do a new calculation? [Y/N] ")

            else:
                print("Suggested DN(s):", dl,"mm. The calculated velocity(s) for the proposed DN(s) is (are) as follows:", vl, "m/s.")
                print("Recommended value: {:.2f}-{:.2f} m/s.".format(v1,v2))
                con = input("Would like to do a new calculation? [Y/N] ")

    if c == "SB" or c == "PB":
        vmin = 3
        vmax = 6
        v(vmin, vmax)

    elif c == "SW":
        vmin = 0.7
        vmax = 1.1
        v(vmin, vmax)

    elif c == "PW":
        vmin = 1.7
        vmax = 2.1
        v(vmin, vmax)

    elif c == "SS" or c == "PS":
        vmin = 1.1
        vmax = 2.1
        v(vmin, vmax)

    else:
        con = input("Entered medium is incorrect.\nWould like to do a new calculation? [Y/N] ")






