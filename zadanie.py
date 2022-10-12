



if __name__ == '__main__':
    print('''
        Zaimplementuj system ratingowy, w którym można oceniać restauracje w trzech kategoriach:
        - smak jedzenia
        - wielkość porcji
        - jakość obsługi
        W każdej z kategorii można przydzielić ocenę w skali pięciogwiazdkowej (od jednej do pięciu gwiazdek),
        gdzie jedna gwiazdka odpowiada ocenie -1, a pięć gwiazdek 3. Aby dodać jedną ocenę, należy przydzielić
        gwiazdki w każdej z kategorii.
        Oceniając restaurację należy podać również wysokość rachunku.

        System powinien zapamiętywać wszystkie oceny (w sposób permanentny lub ulotny - wg. uznania).

        Oceniając zadanie wywołamy przykładową sekwencję funkcji:

        rate_restaurant(restaurant_id, bill_value, taste, size, service)
        rate_restaurant(restaurant_id, bill_value, taste, size, service)
        rate_restaurant(restaurant_id, bill_value, taste, size, service)

        Poza funkcją rate_restaurant należy zaimplementować funkcje:

            def get_rating_history(restaurant_id):
                # zwracającą wszystkie oceny cząstkowe dotyczące restauracji (wraz z datą dodania oceny).
                ...

            def get_rating(restaurant_id):
                # zwracającą dla każdej z kategorii dwa wyniki:
                #   - float oznaczający sumę punktów ratingowych, gdzie punkt ratingowy to iloczyn oceny cząstkowej i wysokości rachunku
                #   - string wyświetlający liczbę gwiazdek (od '*' do '*****'), gdzie liczba gwiazdek wynika ze średniej ważonej ocen cząstkowych (ważenie po wysokości rachunku)
                # oraz analogiczne dwa wyniki będące średnią wyników ze wszystkich kategorii
                ...
        ''')
