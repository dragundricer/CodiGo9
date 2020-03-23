import { Sequelize, ModelType } from 'sequelize';
import { habitacion_model } from '../models/Habitacion';
import { usuario_model } from '../models/Usuario';
import { caracteristica_model } from '../models/Caracteristica';
import { imagenes_model } from '../models/Imagenes';
import { reserva_model } from '../models/Reserva';
import { habitacion_caracteristica_model } from '../models/HabitacionCaracteristica';
export const conexion = new Sequelize(
    'hoteles', 'root', 'root', {
    host: 'localhost',
    dialect: 'mysql',
    // evita que se muestre los comandos sql por consola
    // logging: console.log,
    logging: false,
    dialectOptions: {
        useUTC: true,
        dateString: true,
        typeCast: true
    },
    timezone: '-05:00'
}
)

export const Habitacion: ModelType = habitacion_model(conexion);
export const Usuario: ModelType = usuario_model(conexion);
export const Caracteristica: ModelType = caracteristica_model(conexion);
export const Imagenes: ModelType = imagenes_model(conexion);
export const Reserva: ModelType = reserva_model(conexion);
export const Habitacion_Caracteristica: ModelType = habitacion_caracteristica_model(conexion);

Habitacion.hasMany(Imagenes, {foreignKey: "hab_id"});
Imagenes.belongsTo(Habitacion, {foreignKey: "hab_id"});

Habitacion.hasMany(Habitacion_Caracteristica, {foreignKey:"hab_id"});
Habitacion_Caracteristica.belongsTo(Habitacion, {foreignKey:"hab_id"});

Habitacion.hasMany(Reserva, {foreignKey:"hab_id"});
Reserva.belongsTo(Habitacion, {foreignKey:"hab_id"});

Caracteristica.hasMany(Habitacion_Caracteristica, {foreignKey:"carac_id"});
Habitacion_Caracteristica.belongsTo(Caracteristica, {foreignKey:"carac_id"})

Usuario.hasMany(Reserva, {foreignKey:"usu_id"});
Reserva.belongsTo(Usuario, {foreignKey:"usu_id"});