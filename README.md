## Run project ##

`docker-compose -f /home/atterratio/PycharmProjects/HookBackendTest/docker-compose.yml up -d`

## Admin ##

For test purposes superuser `admin` with password `password` was created.

## Endpoints ##
Open `http://localhost/swagger/` to see available endpoints.

## Условия ##

### Псевдорулетка ###

Есть псевдорулетка с джекпотом, которая состоит из 11 ячеек:
 - числа от 1 до 10
 - ячейка джекпот

Пользователь крутит рулетку и ему выпадает одна из ячеек.
После того, как ячейка выпала, она исключается из дальнейшего выпадения
(т.е. в этом раунде рулетки она уже выпасть не может).
Ячейка джекпот выпадает только после того как выпали все ячейки от 1 до 10.
После того, как выпадает джекпот, раунд рулетки завершается и начинается новый раунд.



