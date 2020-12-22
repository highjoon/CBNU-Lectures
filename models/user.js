const sequelize = require('sequelize');

module.exports = class User extends sequelize.Model {
  static init(sequelize) {
    return super.init({
      email: {
        type: sequelize.STRING(40),
        allowNull: false,
        unique: true,
      },
      nick: {
        type: sequelize.STRING(15),
        allowNull: false,
      },
      password: {
        type: sequelize.STRING(100),
        allowNull: true,
      },
      money: {
        type: sequelize.INTEGER,
        allowNull: false,
        defaultValue: 0,
      },
    }, {
      sequelize,
      timestamps: true,
      paranoid: true,
      modelName: 'User',
      tableName: 'users',
      charset: 'utf8',
      collate: 'utf8_general_ci',
    });
  }

  static associate(db) {
    db.User.hasMany(db.Auction);
  }
};

