saldo_awal = 50_000
deposit = input('berapa anda ingin deposit? ')

saldo_total = saldo_awal + int(deposit)
hutang = 90_000

saldo_sekarang = saldo_total - hutang

if saldo_total == hutang:
    print('thnkyu ya bro')
elif saldo_total >= hutang:
    print('duit kamu masih sisa ' + str(saldo_sekarang) + ", thnkyu ya bro")
else:
    print('duit kamu kan ' + str(saldo_total) + ', ya kurang '+ str(hutang - saldo_total) + ' bang, kan utang kamu ' + str(hutang))


