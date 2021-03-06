import { Habitacion, Tipo } from '../config/sequelize';
import { Request, Response } from 'express';
import { Model } from 'sequelize/types';

export const getAllHabitacion = (req: Request, res: Response) => {
    Habitacion.findAll({
        // Si deseamos excluir uno o mas campos se usa el metodo exclude dentro de la declaracion de los atributos
        attributes: {exclude: ['createdAt', 'updatedAt','tipo_id']},
        // Si deseamos especificar que campos mostrar se usa el metodo include dentro de la declaracion de los atributos
        // attributes: {include: ['hab_nom','hab_disp','hab_prec']},
        // NOTA: Se recomienda usar uno o el otro, puesto que al usar los dos es redundante
        include:[
            {model: Tipo, attributes: ['tipo_desc']}
        ]
    }).then((habitaciones: Model) => {
        console.log(habitaciones);
        if (habitaciones.length === 0) {
            return res.status(200).json({
                ok: true,
                message: 'No hay ninguna habitacion registrada'
            })
        }
        else {
            return res.status(200).json({
                ok: true,
                content: habitaciones
            })
        }
    })
}
export const createHabitacion = (req: Request, res: Response) => {
    // 1. validar el token (que esté vivo)
    // 2. Obtener información del cuerpo del TOKEN 
    // 2.1. Obtener el id del usuario que está enviando el TOKEN del PAYLOAD
    // 3. Validar si el tipo de usuario es "admin" para que pueda crear la habitación
    let objHabitacion = Habitacion.build(req.body);
    Tipo.findByPk(req.body.tipo_id).then((objTipo:Model)=>{
        if(objTipo){
            return objHabitacion.save();
        }else{
            res.status(200).json({
                ok: false,
                content: `El tipo con id ${req.body.tipo_id} no existe en la bd`
            });
        }
    }).then((objHabitacionC: Model) => {
        if (objHabitacionC){
            res.status(201).json({
                ok: true,
                content: objHabitacionC
            })
        }
    }).catch((error: any) => {
        res.status(500).json({
            ok: false,
            message: error
        })
    })
}

